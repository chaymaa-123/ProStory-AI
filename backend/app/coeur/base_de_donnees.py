"""
FICHIER : base_de_donnees.py
OBJECTIF : Configuration de la connexion Supabase PostgreSQL.
CE QU'IL FAUT FAIRE ICI :
1. Gérer la connexion au client Supabase.
2. Fournir le client aux repositories et services.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

# 1. On localise le fichier .env
# Ce code remonte de : base_de_donnees.py -> coeur -> app -> backend
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

# 2. On charge les variables en mémoire
load_dotenv(dotenv_path=ENV_PATH)

# 3. On récupère les valeurs depuis l'environnement système
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# 4. Vérification de sécurité
if not url or not key:
    raise ValueError(f"❌ Erreur : Variables SUPABASE_URL et SUPABASE_KEY introuvables dans {ENV_PATH}")

# 5. Création du client unique pour le projet
supabase: Client = create_client(url, key)

print("✅ Connexion à Supabase configurée.")
