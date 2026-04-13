"""Point d'entrée principal de l'API FastAPI"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import experiences_api
from .coeur.base_de_donnees import engine, Base

# Créer les tables au démarrage
Base.metadata.create_all(bind=engine)

# Initialiser FastAPI
app = FastAPI(
    title="ProStory-AI API",
    description="API pour le partage d'expériences professionnelles",
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

# Inclure les routeurs
app.include_router(experiences_api.router)


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur ProStory-AI API", "docs": "/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
