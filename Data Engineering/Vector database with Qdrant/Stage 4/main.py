from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
import openai
import re
from qdrant_client.http.models import FieldCondition, Filter, MatchText


load_dotenv() 

COLLECTION_NAME = 'arxiv_papers'
QDRANT_HOST = 'localhost'
QDRANT_PORT = 6333

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL')


def extract_author(query: str, pattern=r'by\s+([A-Za-z\s\-]+)') -> str | None:
    return re.findall(pattern, query)


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


def make_query(embedding: list, author_name: str | None):

    query_filter = None
    if author_name:
        query_filter = Filter(must=[FieldCondition(key="authors", match=MatchText(text=author_name))])

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=3,
        with_payload=True,
        with_vectors=False,
        query_filter=query_filter
    )
    return response


if __name__ == '__main__':
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    query = "Mentions of point clouds by Tian-Xing Xu"
    embedding = request_embedding(query)
    author_name = extract_author(query)[0]
    response = make_query(embedding, author_name)


    ids = []
    for point in response.points:
        ids.append(point.payload['id'])
    print(ids)