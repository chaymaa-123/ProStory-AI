import jwt
import os
from datetime import datetime, timedelta
from typing import List, Optional, Any
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from app.coeur.base_de_donnees import supabase 
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION SÉCURITÉ ---
SECRET_KEY = os.getenv("JWT_SECRET", "pfa_prostory_secret_2026_top_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 

from fastapi import APIRouter, status

router = APIRouter(prefix="/auth", tags=["Authentification"])

# --- MODÈLES DE DONNÉES ---
class UserRegister(BaseModel):
    """Modèle pour l'inscription d'un nouvel utilisateur."""
    name: str
    email: EmailStr
    password: str
    role: str = "user"

class UserLogin(BaseModel):
    """Modèle pour la connexion."""
    email: EmailStr
    password: str

class ProfileUpdate(BaseModel):
    """Modèle complet pour la mise à jour du profil (utilisé dans l'onboarding)."""
    nom: Optional[str] = None
    prenom: Optional[str] = None
    age: Optional[int] = None
    statut: Optional[str] = None
    domaine_activite: Optional[str] = None
    poste_actuel: Optional[str] = None
    current_company_id: Optional[str] = None
    annees_experience: Optional[int] = None
    bio: Optional[str] = None
    site_web: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    competences: Optional[List[str]] = []
    centres_interet: Optional[List[str]] = []
    langues: Optional[List[str]] = []
    env_travail_prefere: Optional[List[str]] = []
    points_de_douleur: Optional[List[str]] = []
    ville: Optional[str] = None
    recherche_active: Optional[bool] = None
    is_onboarding_complete: Optional[bool] = None
    views_count: Optional[int] = None
    nom_entreprise: Optional[str] = None
    projets_realises: Optional[Any] = None
    parcours_pro: Optional[Any] = None

# --- FONCTIONS UTILITAIRES ---
def create_access_token(data: dict):
    """Génère un token JWT valide pour une session utilisateur."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- LOGIQUE MÉTIER ---

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_new_user(user_data: UserRegister):
    """
    Crée un nouvel utilisateur dans Supabase Auth.
    Retourne un token pour une connexion automatique immédiate.
    """
    try:
        # 1. Inscription dans Supabase Auth (Gère l'email/password)
        auth_response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password,
            "options": {"data": {"full_name": user_data.name, "role": user_data.role}}
        })

        if not auth_response.user:
            raise HTTPException(status_code=400, detail="Échec de la création du compte.")

        # 2. Récupération des infos (le trigger SQL a déjà créé l'entrée dans 'public.users')
        profile = supabase.table("users").select("*").eq("id", auth_response.user.id).single().execute()

        # 3. Génération du Token pour l'auto-login
        token = create_access_token(data={
            "sub": auth_response.user.email, 
            "id": auth_response.user.id, 
            "role": user_data.role
        })

        return {
            "status": "success",
            "access_token": token,
            "token_type": "bearer",
            "user": profile.data or {"id": auth_response.user.id, "email": auth_response.user.email, "role": user_data.role}
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
def login_user(login_data: UserLogin):
    """Vérifie les identifiants et retourne un token de session."""
    try:
        # Vérification via Supabase Auth
        auth_res = supabase.auth.sign_in_with_password({"email": login_data.email, "password": login_data.password})
        
        if not auth_res.user:
            raise HTTPException(status_code=401, detail="Identifiants incorrects.")

        # Récupération du rôle et des infos dans la table public.users
        profile = supabase.table("users").select("*").eq("id", auth_res.user.id).single().execute()
        
        token = create_access_token(data={
            "sub": auth_res.user.email, 
            "id": auth_res.user.id, 
            "role": profile.data.get("role") if profile.data else "user"
        })

        return {"access_token": token, "token_type": "bearer", "user": profile.data}
    except Exception:
        raise HTTPException(status_code=401, detail="Email ou mot de passe invalide.")

@router.put("/profile/update/{user_id}")
def update_user_profile(user_id: str, profile_data: ProfileUpdate):
    """
    Met à jour ou crée le profil utilisateur (Onboarding).
    Utilise 'upsert' pour être sûr que l'entrée existe.
    """
    try:
        # On prépare les données de base
        update_dict = {
            "id": user_id,
            "is_onboarding_complete": True,
            "updated_at": datetime.utcnow().isoformat()
        }
        
        # On ajoute dynamiquement tous les champs non-nuls envoyés par le front
        new_data = profile_data.dict(exclude_unset=True)
        update_dict.update(new_data)

        # On enregistre dans la table 'profiles'
        supabase.table("profiles").upsert(update_dict).execute()

        return {"status": "success", "message": "Profil synchronisé avec succès !"}
    except Exception as e:
        print(f"ERROR PROFILE UPDATE: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Erreur de synchronisation : {str(e)}")

@router.get("/profile/{user_id}")
def get_user_profile(user_id: str):
    """Récupère toutes les infos du profil pour l'affichage."""
    try:
        res = supabase.table("profiles").select("*").eq("id", user_id).single().execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Profil introuvable")
        return res.data
    except Exception as e:
        raise HTTPException(status_code=404, detail="Erreur de récupération")