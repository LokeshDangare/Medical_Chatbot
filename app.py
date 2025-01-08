import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain.vectorstores import Pinecone
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *


app = Flask(__name__)

_ = load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]

embeddings = download_embeddings()

index_name = "medical"

docsearch = Pinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.4, max_tokens=500)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
