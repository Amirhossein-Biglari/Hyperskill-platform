from qdrant_client import QdrantClient

COLLECTION_NAME = 'arxiv_papers'
QDRANT_HOST = 'localhost'
QDRANT_PORT = 6333


def similar_items(collection_name: str, paper_id: str, num_similar_items: int = 5):

    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    paper_search_result = client.scroll(
        collection_name=collection_name,
        scroll_filter={
            "must": [
                {
                    'key': 'id',
                    'match': {
                        'value': paper_id
                    }
                }
            ]
        },
        limit=1,
        with_vectors=True
    )

    if paper_search_result:
        first_result = paper_search_result[0]
        first_record = first_result[0]
        embedding = first_record.vector

        top_five = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=embedding,
            limit=num_similar_items,
            with_payload=True,
            with_vectors=False
        )
        top_five_ids = []
        for record in top_five:
            top_five_ids.append(record.payload['id'])
        print(top_five_ids)
    else:
        print(f"The vector for the Paper with id `{paper_id}`, wasn't found")


if __name__ == '__main__':
    PAPER_ID = '1311.5068'
    similar_items(COLLECTION_NAME, PAPER_ID)
