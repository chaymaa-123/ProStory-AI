
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth import UserRegister, register_new_user, UserLogin, login_user 
from app.ai.analytics import router as ai_router 

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

# Inclure le routeur IA
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
