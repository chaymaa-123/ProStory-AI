"""
FICHIER : repo_experience.py
OBJECTIF : Requêtes SQL SQLAlchemy liées aux expériences.
CE QU'IL FAUT FAIRE ICI :
1. Ajouter une fonction `obtenir_toutes_experiences(db, limites, offset)`.
2. Ajouter une fonction de recherche sémantique utilisant `pgvector` (ORDER BY embedding <-> vecteur_recherche).
"""

"""
1. Objectif : Isoler les requêtes SQL/SQLAlchemy.
2. Contenu prévu : Fonctions CRUD (Créer, trouver par similarité d'embedding).
3. Responsable : Backend / Database.
4. Interactions : Interroge les modèles, appelé par les services.
5. Checklist :
   - [ ] Coder trouver_experiences_similaires(db, vecteur)
"""

from sqlalchemy.orm import Session

# Fonctions de requetes DB pour Experience
