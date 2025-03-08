import json
import uuid
from typing import Any, Generator

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

COLLECTION_NAME = 'arxiv_papers'
VECTOR_DIMENSION = 1536
EMBEDDING_MODEL = 'text-embedding-ada-002'
EMBEDDING_FILE_PATH = 'ml-archxiv-embeddings/ml-arxiv-embeddings.json'
QDRANT_HOST = 'localhost'
QDRANT_PORT = 6333

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

if not client.collection_exists(collection_name=f"{COLLECTION_NAME}"):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={"size": VECTOR_DIMENSION, "distance": "Cosine"},
    )


def stream_json(file_path) -> Generator[Any, Any, None]:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def load_vectors_to_qdrant(file_path, batch_size=500) -> None:
    batch = []
    total_records = 0

    for record in stream_json(file_path):
        payload = record.copy()
        payload.pop("embedding", None)
        if not record.get("embedding", None):
            print(
                f"Warning: Record {record.get('id', 'unknown')} is missing embedding."
            )
            continue

        point = PointStruct(
            id=str(uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name=record["id"])),
            vector=record.get("embedding", None),
            payload=payload,
        )
        batch.append(point)

        if len(batch) >= batch_size:
            client.upsert(collection_name=COLLECTION_NAME, wait=True, points=batch)
            total_records += len(batch)
            batch = []
            print(f"Inserted {total_records} records...")

    if batch:
        client.upsert(collection_name=COLLECTION_NAME, wait=True, points=batch)
        total_records += len(batch)
        batch = []
        print(
            f"Inserted remaining {len(batch)} records. Total records: {total_records}"
        )

    print(f"Total records inserted: {total_records}")

if __name__ == '__main__':
    ...
    load_vectors_to_qdrant(EMBEDDING_FILE_PATH)
    print("All records have been inserted into the Qdrant collection.")