"""
FICHIER : experience_schema.py
OBJECTIF : Modèles Pydantic pour valider les données entrantes/sortantes des Expériences.
CE QU'IL FAUT FAIRE ICI :
1. Ajouter des validateurs stricts (ex: longueur minimale du contenu).
2. Créer `ExperienceUpdate` pour la modification des posts.
"""

"""
1. Objectif : Valider les données entrantes/sortantes des requêtes HTTP.
2. Contenu prévu : Classes Pydantic (ExperienceCreate, ExperienceResponse).
3. Responsable : Backend.
4. Interactions : Utilisé par les routes.
5. Checklist :
   - [ ] Créer ExperienceCreate (titre, texte, tags)
"""

from pydantic import BaseModel

# class ExperienceBase(BaseModel):
#     pass
