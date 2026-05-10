"""Configuration de la connexion Supabase PostgreSQL."""

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
# On utilise la SERVICE_ROLE_KEY en priorité pour bypasser RLS côté backend
key: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

# Fallback sur SUPABASE_KEY si la clé service role est absente ou non configurée
if not key or key == "your-service-role-key-here":
    key = os.getenv("SUPABASE_KEY")

# 4. Vérification et Initialisation
supabase: Client = None

if not url or not key or key == "your-service-role-key-here":
    print("⚠️  AVERTISSEMENT : Variables SUPABASE_URL ou SUPABASE_KEY manquantes.")
    print("Le backend démarrera mais les fonctionnalités liées à la base de données seront indisponibles.")
else:
    try:
        # 5. Création du client unique pour le projet
        supabase = create_client(url, key)
        print("✅ Connexion à Supabase configurée avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors de l'initialisation du client Supabase : {str(e)}")

# Note : Dans les repositories, il faudra vérifier si 'supabase' n'est pas None avant usage.
