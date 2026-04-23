from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import experiences_api
from .routes import company_api
from .ai import analytics as ai_analytics, router as ai_router
from app.auth import router as auth_router

# Initialiser FastAPI
app = FastAPI(
    title="ProStory-AI API",
    description="API pour le partage d'expériences professionnelles",
    version="0.1.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routeurs
app.include_router(auth_router, prefix="/api")
app.include_router(experiences_api.router)
app.include_router(company_api.router)
app.include_router(ai_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur ProStory-AI API", "docs": "/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}