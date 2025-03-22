from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
import openai


load_dotenv() 

COLLECTION_NAME = 'arxiv_papers'
QDRANT_HOST = 'localhost'
QDRANT_PORT = 6333

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL')


def request_embedding(query: str) -> list:
    openai_client = openai.OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL,
    )

    query = query.replace('\n', '')

    response = openai_client.embeddings.create(
        model="text-embedding-ada-002",
        input=query
    )

    embedding = response.data[0].embedding

    return embedding


def top_five_similar(embedding: list) -> list:
    top_five = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=5,
        with_payload=True,
        with_vectors=False
    )

    top_five_ids = []
    for record in top_five.points:
        top_five_ids.append(record.payload['id'])

    return top_five_ids


if __name__ == '__main__':
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    query = "the attention mechanism in deep learning"
    embedding = request_embedding(query)

    top_five_ids = top_five_similar(embedding)
    print(top_five_ids)