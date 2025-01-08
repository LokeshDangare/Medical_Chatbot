# Medical_Chatbot

## Project Overview

A medical chatbot is a conversational AI-powered program that provides healthcare-related information and assistance to patients. In this project, I have used custom medical dataset to develop effective chatbot.

### Technology
1. Python
2. LLM - Google Gemini Pro
3. LangChain
4. VectorDB- Pinecone or FAISS
5. Github
6. Embedding Model - GoogleGenerativeAIEmbeddings

## How to run?

#### Step 01 - Clone the repository
```bash
Project repo: https://github.com/
```

### Step 02 - Create a conda environment after opening the repository in git bash or terminal

```bash
conda create -n medchat python=3.11 -y
```

```bash
conda activate medchat
```

### Step 03 - Install all requirements
```bash
pip install -r requirements.txt
```

### Step 04 - Execute store_index.py file for storing embeddings in pinecone

Execute it only one time for same data and if you change the data then only you need to execute it again.

```bash
python store_index.py
```

### Step 05 - Run an application.

``` bash
python app.py
```

