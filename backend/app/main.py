"""Point d'entrée principal de l'API FastAPI"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import experiences_api
from app.auth import UserRegister, register_new_user, UserLogin, login_user

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
    """
    Vérifie si l'API est fonctionnelle.

    Returns:
        dict: {status: ok}
    """
    return {"status": "ok"}

@app.post("/auth/register")
async def register(user: UserRegister):
    """
    Enregistre un nouvel utilisateur.

    Args:
        user (UserRegister): Informations de l'utilisateur à enregistrer.

    Returns:
        dict: Informations de l'utilisateur enregistré.
    """
    return register_new_user(user)

@app.post("/auth/login")
async def login(credentials: UserLogin):
    """
    Connecte un utilisateur existant.

    Args:
        credentials (UserLogin): Informations de connexion de l'utilisateur.

    Returns:
        dict: Informations de l'utilisateur connecté.
    """
    return login_user(credentials)
