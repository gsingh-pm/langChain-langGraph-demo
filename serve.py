from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from pydantic import BaseModel
from operator import itemgetter
# Imports to serve the app as an API
from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables import RunnableLambda


load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

class ChatRequest(BaseModel):
    input: str

class ChatResponse(BaseModel):
    answer: str

loader = WebBaseLoader("https://www.policyme.com/blog/best-life-insurance-in-canada")
insurance_doc = loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
final_documents=text_splitter.split_documents(insurance_doc)

embedding=OpenAIEmbeddings(model="text-embedding-3-large")

vectorstore = Chroma.from_documents(
    documents=final_documents,
    embedding=embedding,
    persist_directory="chroma_db"  # Directory to persist the vector store
)

llm=ChatOpenAI(model="gpt-5-2025-08-07")

prompt = ChatPromptTemplate.from_template(
    """
     You are an expert insurance advisor.
    Answer the question **only** using the provided context. If the answer isn't in the context, say you don't know.

    Question: {input}

    <context>
    {context}
    </context>
    """
)
document_chain=create_stuff_documents_chain(llm,prompt)

retriever = vectorstore.as_retriever() # retriever to get data from vectorstore DB
retriever_chain = create_retrieval_chain(retriever, document_chain)

answer_chain = (
    retriever_chain
    | itemgetter("answer")
    | RunnableLambda(lambda s: {"answer": s})
)

# app
app = FastAPI(title="Life Insurance Expert Chatbot API", version="1.0", description="An API to answer questions about Life Insurance in Canada")
add_routes(app, answer_chain, path="/chat", input_type=ChatRequest, output_type=ChatResponse)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8005)