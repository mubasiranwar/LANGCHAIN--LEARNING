# query_chroma.py

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 1) Load same embeddings used during building DB
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

# 2) Load existing Chroma DB
persist_dir = "./chroma_db"

vectordb = Chroma(
    persist_directory=persist_dir,
    embedding_function=embeddings,
    collection_name="my_collection"
)

# 3) Query
query = "What is the name of person about which data is?"
results = vectordb.similarity_search(query, k=3)

# 4) Print results
for r in results:
    print("-----")
    print(r.page_content)
