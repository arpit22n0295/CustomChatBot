# fastapi_app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str 
    name : str = "Mohit"

@app.post("/api/query")
def query_backend(q: Query):
    # Simulate AI/RAG response
    answer = f"AI answer to: {q.question}"
    sources = ["doc1.pdf", "doc2.pdf"]
    return {"answer": answer, "sources": sources}

@app.get("/about")
def about(q: str = Query(default=None)):
    return {"name": "Arpit Arya", "Job": "AI/ML Engineer", "query_received": q} 