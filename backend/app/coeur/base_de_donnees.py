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
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration de la base de donnees ici

Base = declarative_base()
