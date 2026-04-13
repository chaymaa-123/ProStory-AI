import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from app.coeur.base_de_donnees import supabase 
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION SÉCURITÉ ---
SECRET_KEY = os.getenv("JWT_SECRET", "pfa_prostory_secret_2026_top_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # Expire après 24 heures

# --- MODÈLES DE DONNÉES ---
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# --- FONCTIONS UTILITAIRES ---
def hash_password(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compare le mot de passe en clair avec le hash stocké"""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict):
    """Génère le Token JWT (Badge d'accès)"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- LOGIQUE MÉTIER ---
def register_new_user(user_data: UserRegister):
    try:
        check = supabase.table("users").select("email").eq("email", user_data.email).execute()
        if check.data and len(check.data) > 0:
            raise HTTPException(status_code=400, detail="Cet email est déjà enregistré.")

        hashed_password = hash_password(user_data.password)

        new_user = {
            "name": user_data.name,
            "email": user_data.email,
            "password": hashed_password,
            "role": user_data.role
        }

        result = supabase.table("users").insert(new_user).execute()
        
        if not result.data or len(result.data) == 0:
            raise HTTPException(status_code=500, detail="Échec de l'enregistrement.")
            
        return {
            "status": "success",
            "message": "Utilisateur créé avec succès !",
            "user": {
                "id": result.data[0].get("id"),
                "email": result.data[0].get("email"),
                "name": result.data[0].get("name")
            }
        }
    except Exception as e:
        print(f"DEBUG ERROR REGISTER: {str(e)}")
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail="Une erreur interne est survenue.")

def login_user(login_data: UserLogin):
    """Vérifie les accès et renvoie un Token JWT"""
    result = supabase.table("users").select("*").eq("email", login_data.email).execute()
    
    if not result.data:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect.")

    user = result.data[0]

    # Correction : Utilisation de verify_password définie plus haut
    if not verify_password(login_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect.")

    # Correction : Utilisation de create_access_token définie plus haut
    token = create_access_token(data={
        "sub": user["email"], 
        "id": user["id"], 
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "name": user["name"],
            "role": user["role"]
        }
    }