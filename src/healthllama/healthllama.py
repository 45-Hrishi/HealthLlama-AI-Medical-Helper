import os
from dotenv import load_dotenv
from healthllama.store_vectors import AddToDatabase
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from healthllama.utils import create_embeddings,load_model,load_prompt,is_index_present,get_vector_store
from langchain_pinecone.vectorstores import PineconeVectorStore

load_dotenv()

index_name = "healthllama"
    
def get_response(user_input):
    if not is_index_present(index_name):
        embeddings = create_embeddings()
        vector_store = AddToDatabase(index_name=index_name,embeddings=embeddings)
    
    vector_store = get_vector_store(index_name)
    retriever = vector_store.as_retriever(search_kwargs={'k':2})
    llama_model = load_model("model/llama-2-7b.Q4_K_M.gguf")
    prompt = load_prompt("prompts.md")
    
    question_answer_chain = create_stuff_documents_chain(llama_model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    results = rag_chain.invoke({"input": f"{user_input}"})
    return results["answer"]
