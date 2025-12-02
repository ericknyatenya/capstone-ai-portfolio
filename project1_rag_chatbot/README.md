# Project 1 — RAG Chatbot

Overview

This project demonstrates a retrieval-augmented generation chatbot built with embeddings, a vector store (FAISS/Chroma), and an LLM for generation. Includes notebooks, a demo API, and deployment instructions.

## Contents

- `notebooks/` — walkthroughs and examples
- `src/` — chunking, embedding, retriever modules
- `deployments/` — Dockerfile for containerized deployment
- `tests/` — smoke tests

## Setup

```bash
cd project1_rag_chatbot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Demo

```bash
cd project1_rag_chatbot
PYTHONPATH=.. python -c "
from src.chunker import chunk_text
from src.embedder import Embedder
from src.retriever import Retriever

# Load and chunk a document
text = 'The Apollo 11 mission landed on the Moon in 1969. Neil Armstrong and Buzz Aldrin walked on the lunar surface.'
chunks = chunk_text(text, chunk_size=15, overlap=3)
print(f'Created {len(chunks)} chunks')

# Embed and index
emb = Embedder()
vectors = emb.embed(chunks)
ret = Retriever()
ret.add(chunks, vectors)

# Query
query_vec = emb.embed(['Who walked on the Moon?'])[0]
results = ret.retrieve(query_vec, top_k=2)
print('\\nTop retrieved chunks:')
for idx, score, text in results:
    print(f'  [{score:.3f}] {text}')
"
```

Expected output:
```
Created 2 chunks
Top retrieved chunks:
  [0.707] The Apollo 11 mission landed on the Moon in 1969. Neil Armstrong and Buzz
  [0.500] Aldrin walked on the lunar surface.
```

## Docker

```bash
docker build -t rag-chatbot deployments/
docker run -p 8000:8000 rag-chatbot
```

## Key Concepts

- **Chunking**: Split documents into overlapping text segments.
- **Embedding**: Convert text chunks into fixed-dimension vectors.
- **Retrieval**: Find most similar chunks using cosine similarity.
- **Generation**: Feed retrieved context to an LLM for response synthesis.
