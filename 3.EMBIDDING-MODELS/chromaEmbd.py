# chromaEmbd.py

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# 1) Load documents
loader = TextLoader("3.EMBIDDING-MODELS/example.txt")
docs = loader.load()

# 2) Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# 3) HuggingFace Embeddings (New)
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

# 4) Create persistent Chroma DB
persist_dir = "./chroma_db"

vectordb = Chroma(
    persist_directory=persist_dir,
    embedding_function=embeddings,
    collection_name="my_collection"
)

# 5) Add documents
vectordb.add_documents(chunks)

# ❌ NO vectordb.persist() — remove it!

print("Vector store saved at:", persist_dir)
