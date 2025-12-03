# 🌟 LangChain Practice Repository

**Hands-on LLMs, Chat Models, Embeddings, RAG, ChromaDB & Agentic AI**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/LangChain-Latest-yellow?logo=chainlink" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20DB-green?logo=database" />
  <img src="https://img.shields.io/badge/HuggingFace-Models-orange?logo=huggingface" />
  <img src="https://img.shields.io/badge/OpenRouter-LLMs-purple?logo=apacheairflow" />
</p>

---

## 📘 Overview

This repository contains my **complete learning journey** with **LangChain**, featuring real, practical, production-ready examples of:

- ✅ LLM initialization & prompt engineering
- ✅ Chat models (OpenRouter, Gemini, HuggingFace)
- ✅ Chains & RunnableSequences (LCEL)
- ✅ Embeddings & vector similarity
- ✅ Vector databases (ChromaDB)
- ✅ PDF/Text document loaders
- ✅ Query pipelines & retrieval
- ✅ Structured outputs with Pydantic
- ✅ RAG-ready code examples

All code is organized cleanly for **industry-level learning** and hands-on practice.

---

## 📂 Folder Structure
```
LANGCHAIN/
│
├── 1.LLMS/
│   └── llm.py                          # Basic LLM initialization
│
├── 2.CHATS-MODELS/
│   ├── chain.py                        # Basic chains
│   ├── chatmodel.py                    # OpenRouter chat model
│   ├── conditional.py                  # Conditional routing
│   ├── hugging_face_chatmodel.py       # HuggingFace chat integration
│   ├── gemini.py                       # Google Gemini chat
│   ├── parallel_chain.py               # Parallel chain execution
│   ├── runablesequence.py              # LCEL RunnableSequence
│   └── strutureout.py                  # Structured output with Pydantic
│
├── 3.EMBIDDING-MODELS/
│   ├── chromaEmbd.py                   # Embedding creation & storage
│   ├── example.txt                     # Sample text file
│   ├── Notes.pdf                       # Sample PDF
│   └── query_chroma.py                 # Vector search queries
│
├── 4.CHOROMADB/
│   └── p1.py                           # ChromaDB basics
│
├── 5.Documents_loader/
│   ├── Directory_load.py               # Load multiple files from directory
│   ├── adden_load.py                   # Advanced document loading
│   ├── cricket.txt                     # Sample text
│   ├── Andrew Ng Deep Learning Notes.pdf
│   └── How To Use AI Agents in 2025.pdf
│
└── .venv/                              # Virtual environment (local only)
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com//.git
cd 
```

### 2️⃣ Create & Activate Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=your_openrouter_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here
GOOGLE_API_KEY=your_gemini_key_here  # Optional
```

---

## 🔥 Featured Topics

### 💬 LLMs & ChatModels
- OpenRouter LLM integration
- HuggingFace ChatModels
- Google Gemini
- Structured output with Pydantic
- Conditional routing & branching

### ⚙️ Chains
- Basic LangChain chains
- Parallel chain execution
- RunnableSequence (LCEL)
- Custom chain logic

### 🧠 Embeddings
- Sentence Transformers
- Creating & storing embeddings
- Document similarity search
- Vector-based retrieval

### 🗂️ Document Loading
- PDF loader (PyPDF)
- Directory loader (batch processing)
- TXT file loader
- Preprocessing for RAG pipelines

### 🗄️ Vector Store
- ChromaDB setup
- Creating collections
- Querying vectors
- Persistent database storage

---

## 📊 Technologies Used

| Category | Tools |
|----------|-------|
| **LLMs** | OpenRouter, Gemini, HuggingFace |
| **Framework** | LangChain, LCEL |
| **Vector DB** | ChromaDB |
| **Embeddings** | Sentence Transformers, HuggingFace |
| **Language** | Python 3.10+ |
| **Utilities** | python-dotenv, Pydantic, PyPDF |

---

## 🛠️ Run Examples

### ▶️ Basic ChatModel
```bash
python 2.CHATS-MODELS/chatmodel.py
```

### ▶️ Load Directory of Documents
```bash
python 5.Documents_loader/Directory_load.py
```

### ▶️ Query ChromaDB
```bash
python 3.EMBIDDING-MODELS/query_chroma.py
```

### ▶️ Structured Output
```bash
python 2.CHATS-MODELS/strutureout.py
```

---

## 🚧 Future Additions

- [ ] Full Agent-based Tool Calling
- [ ] Complete RAG Pipeline (End-to-End)
- [ ] Streamlit Chatbot UI
- [ ] FastAPI Backend
- [ ] Automatic RAG evaluation (RAGAS)
- [ ] Multi-query retrieval
- [ ] Re-ranking with Cohere/BGE
- [ ] LangGraph workflows

---

## 🤝 Contributing

Pull requests and suggestions are always welcome! Feel free to:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you find this project helpful, please consider giving it a **star ⭐** on GitHub — it helps a lot!

---

## 📧 Contact

**Your Name**  
📧 Email: your.mubasiranwar70@gmail.com 
🔗 LinkedIn:https://www.linkedin.com/in/mubasir-anwar-013628316/?skipRedirect=true)  


---

**Happy Learning! 🚀**
