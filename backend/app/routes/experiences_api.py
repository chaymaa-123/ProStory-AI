"""
FICHIER : experiences_api.py
OBJECTIF : Contrôleurs / Points d'accès (Endpoints) de l'API pour les Expériences.
CE QU'IL FAUT FAIRE ICI :
1. Ajouter l'endpoint `GET /experiences` pour lister le fil d'actualité.
2. Utiliser `Depends(get_utilisateur_actuel)` pour sécuriser la création/modification d'une expérience.
"""

"""
1. Objectif : Exposer les URLs pour gérer le fil d'actualité et la création.
2. Contenu prévu : GET /experiences, POST /experiences.
3. Responsable : Backend.
4. Interactions : Appelle services/, consommé par le Frontend.
5. Checklist :
   - [ ] Créer route protégée pour créer un post
"""

from fastapi import APIRouter

router = APIRouter()
