"""
FICHIER : main.py
OBJECTIF : Point d'entrée principal de l'API FastAPI.
CE QU'IL FAUT FAIRE ICI :
1. Importer et inclure (`app.include_router`) toutes les nouvelles routes (ex: utilisateurs, auth, admin).
2. Configurer les middlewares CORS pour autoriser le frontend en production.
3. Ajouter une gestion globale des exceptions si nécessaire.
"""

"""
1. Objectif : Point d'entrée principal de l'API FastAPI.
2. Contenu prévu : Initialisation de l'application, configuration CORS, inclusion des routeurs.
3. Responsable : Backend.
4. Interactions : Inclut tout le dossier routes/. Connecté au Frontend.
5. Checklist :
   - [ ] Instancier FastAPI
   - [ ] Configurer les middlewares CORS pour React
   - [ ] app.include_router(...) pour l'auth, les expériences, l'admin
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth import UserRegister, register_new_user, UserLogin, login_user 


app = FastAPI()


app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:3000"],       
    allow_credentials=True,
    allow_methods=["*"],             
    allow_headers=["*"],              
)

@app.post("/auth/register")
async def register(user: UserRegister):
    return register_new_user(user)

@app.post("/auth/login")
async def login(credentials: UserLogin):
    return login_user(credentials)