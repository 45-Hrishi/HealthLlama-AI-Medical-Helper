import time
import os
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from uuid import uuid4
from healthllama.utils import split_text
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("PINCONE_API_KEY")

def create_index(api_key,index_name,dimension):
    pc = Pinecone(api_key=api_key)
    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)

    index = pc.Index(index_name)
    return index


def AddToDatabase(index_name,embeddings):
    text_chunks = split_text()
    index_obj = create_index(api_key,index_name=index_name,dimension=384)
    chunks_len = len(text_chunks)
    vector_store = PineconeVectorStore(index=index_obj, embedding=embeddings)
    uuids = [str(uuid4()) for _ in range(chunks_len)]
    vector_store.add_texts(texts=text_chunks,ids=uuids,batch_size=16)
    return vector_store

