"""Version simplifiée du main.py pour tester uniquement le module IA"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.ai.analytics import router as ai_router

# Initialiser FastAPI
app = FastAPI(
    title="ProStory-AI API - Test Module IA",
    description="API pour tester le module IA",
    version="0.1.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure le routeur IA
app.include_router(ai_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "ProStory-AI API - Module IA Test", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "ok", "module": "IA"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
