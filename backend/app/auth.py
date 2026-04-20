import jwt
import os
from datetime import datetime, timedelta
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from app.coeur.base_de_donnees import supabase 
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION SÉCURITÉ ---
# Note : Pour le mode "Firebase", on peut soit continuer à utiliser ton propre JWT 
# soit utiliser celui de Supabase. Pour rester simple avec ton code actuel :
SECRET_KEY = os.getenv("JWT_SECRET", "pfa_prostory_secret_2026_top_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 

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
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- LOGIQUE MÉTIER ---

def register_new_user(user_data: UserRegister):
    """
    INSCRIPTION : On utilise Supabase Auth.
    Le Trigger SQL s'occupera de remplir ta table 'users' automatiquement.
    """
    try:
        # 1. On appelle Supabase Auth
        # On passe le 'name' et le 'role' dans options.data (metadata)
        # pour que le Trigger SQL puisse les récupérer
        auth_response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password,
            "options": {
                "data": {
                    "full_name": user_data.name,
                    "role": user_data.role
                }
            }
        })

        if not auth_response.user:
            raise HTTPException(status_code=400, detail="Erreur lors de la création du compte.")

        return {
            "status": "success",
            "message": "Utilisateur créé ! Le Trigger SQL a généré ton profil.",
            "user": {
                "id": auth_response.user.id,
                "email": auth_response.user.email
            }
        }
    except Exception as e:
        print(f"DEBUG ERROR REGISTER: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

def login_user(login_data: UserLogin):
    """
    CONNEXION : On utilise Supabase Auth pour vérifier l'email/password.
    """
    try:
        # 1. On vérifie les identifiants avec Supabase
        auth_response = supabase.auth.sign_in_with_password({
            "email": login_data.email,
            "password": login_data.password
        })

        if not auth_response.user:
            raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect.")

        # 2. On récupère les infos du profil dans TA table 'public.users' 
        # (car le login Supabase ne donne pas le 'role' personnalisé par défaut)
        profile = supabase.table("users").select("*").eq("id", auth_response.user.id).single().execute()

        # 3. On génère ton Token JWT comme avant
        token = create_access_token(data={
            "sub": auth_response.user.email, 
            "id": auth_response.user.id, 
            "role": profile.data.get("role") if profile.data else "user"
        })

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": profile.data
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Identifiants invalides.")