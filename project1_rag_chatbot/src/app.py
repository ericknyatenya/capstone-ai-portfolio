from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from .chunker import chunk_text
from .embedder import Embedder
from .retriever import Retriever

# Global state
_retriever = None
_embedder = None
_sample_docs = [
    "The Apollo 11 mission landed the first humans on the Moon in 1969.",
    "Neil Armstrong and Buzz Aldrin walked on the lunar surface.",
    "Python is a widely used high-level programming language.",
    "Machine learning enables systems to learn from data and make predictions.",
    "The Amazon rainforest is the largest tropical rainforest in the world.",
]


class QueryRequest(BaseModel):
    query: str
    top_k: int = 3


class QueryResponse(BaseModel):
    query: str
    results: list


app = FastAPI(title="RAG Chatbot API")


@app.on_event("startup")
async def startup():
    global _retriever, _embedder
    # Initialize retriever
    _embedder = Embedder()
    all_chunks = []
    for doc in _sample_docs:
        chunks = chunk_text(doc, chunk_size=15, overlap=3)
        all_chunks.extend(chunks)
    
    vectors = _embedder.embed(all_chunks)
    _retriever = Retriever()
    _retriever.add(all_chunks, vectors)


@app.get("/health")
def health():
    return {"status": "ok", "retriever_ready": _retriever is not None}


@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    if _retriever is None or _embedder is None:
        raise HTTPException(status_code=503, detail="Retriever not initialized")
    
    # Embed query
    qv = _embedder.embed([req.query])[0]
    
    # Retrieve
    results = _retriever.retrieve(qv, top_k=req.top_k)
    
    # Format response
    formatted = [
        {"rank": i+1, "score": float(score), "text": text}
        for i, (_, score, text) in enumerate(results)
    ]
    
    return QueryResponse(query=req.query, results=formatted)
