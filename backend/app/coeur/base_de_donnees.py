"""
FICHIER : base_de_donnees.py
OBJECTIF : Configuration de la connexion PostgreSQL avec SQLAlchemy.
CE QU'IL FAUT FAIRE ICI :
1. Ajuster les paramètres de pool de connexion si l'application grossit.
2. Ne pas toucher à `get_db()` sauf si vous implémentez un système asynchrone (asyncpg).
"""

"""
1. Objectif : Gérer la connexion à PostgreSQL.
2. Contenu prévu : Création de l'engine SQLAlchemy et du model de session.
3. Responsable : Backend / Database.
4. Interactions : Fournit la DB aux repositories.
5. Checklist :
   - [ ] Créer l'engine et la fonction get_db()
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from ..coeur.config import settings

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
    raise ValueError(f"❌ Erreur : Variables introuvables dans {ENV_PATH}")

# 5. Création du client unique pour le projet
supabase: Client = create_client(url, key)

print("✅ Connexion à la base de données configurée via variables d'environnement.")

# Créer l'engine SQLAlchemy
engine = create_engine(
    settings.database_url,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    echo=False
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles ORM
Base = declarative_base()


def get_db():
    """Dépendance pour obtenir la session DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



