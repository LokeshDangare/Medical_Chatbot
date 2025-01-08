from src.helper import load_pdf_file, text_split, download_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain.vectorstores import Pinecone
import os
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]


extracted_data = load_pdf_file(data="Data/")
text_chunks = text_split(extracted_data)
embeddings = download_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical"

pc.create_index(
    name=index_name,
    dimension=768,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

# Embed each chunks and insert the embeddings into your Pinecone index.
docsearch = Pinecone.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)