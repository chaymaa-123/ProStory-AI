from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routes import experiences_api
from .routes import company_api
from .ai import analytics as ai_analytics, router as ai_router
from app.auth import (
    UserRegister, register_new_user, 
    UserLogin, login_user, 
    update_user_profile, ProfileUpdate, 
    get_user_profile
)

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
app.include_router(experiences_api.router)
app.include_router(company_api.router)
app.include_router(ai_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur ProStory-AI API", "docs": "/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/auth/register")
async def register(user: UserRegister):
    return register_new_user(user)

@app.post("/auth/login")
async def login(credentials: UserLogin):
    return login_user(credentials)

@app.put("/auth/profile/update/{user_id}")
async def update_profile(user_id: str, profile_data: ProfileUpdate):
    return update_user_profile(user_id, profile_data)

@app.get("/auth/profile/{user_id}")
async def get_profile(user_id: str):
    return get_user_profile(user_id)