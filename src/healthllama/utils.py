import os
import torch
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.llms.ctransformers import CTransformers
from langchain.embeddings import HuggingFaceEmbeddings
from healthllama.document_processor import get_extracted_text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
load_dotenv()

api_key = os.getenv("PINCONE_API_KEY")


def split_text():
    extracted_text = get_extracted_text()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    text_chunks = text_splitter.split_text(extracted_text)
    return text_chunks

def create_embeddings(model="sentence-transformers/all-MiniLM-L6-v2"):
    model = "sentence-transformers/all-MiniLM-L6-v2"
    DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
    embeddings = HuggingFaceEmbeddings(model_name=model,model_kwargs={"device":DEVICE})
    return embeddings

def is_index_present(index_name):
    api_key = os.getenv("PINCONE_API_KEY")
    print(api_key)
    pc = Pinecone(api_key=api_key)
    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]
    print(existing_indexes)
    return index_name in existing_indexes

def get_vector_store(index_name):
    pc = Pinecone(api_key=api_key)
    index = pc.Index(index_name)
    embeddings = create_embeddings()
    vector_store = PineconeVectorStore(index,embeddings)
    return vector_store
      
def load_prompt(file_path):
    with open(file_path, 'r') as file:
        prompt_template = file.read()
    prompt = PromptTemplate.from_template(prompt_template)
    return prompt

def load_model(model_path):
    model = CTransformers(model=model_path,
                          model_type="llama",
                          config={"temperature" :0.2,'context_length' : 1024})
    return model