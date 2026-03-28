"""
FICHIER : auth_schema.py
OBJECTIF : Modèles Pydantic pour l'authentification (Login, Inscription).
CE QU'IL FAUT FAIRE ICI :
1. Ajouter le modèle `UtilisateurCreate` (email, mot de passe, confirmation).
2. Ajouter le modèle `UtilisateurResponse` (sans le mot de passe hashé !).
"""

"""
1. Objectif : Valider le login/mot de passe.
2. Contenu prévu : Classes Pydantic pour l'authentification.
3. Responsable : Backend.
4. Interactions : Utilisé par les routes d'authentification.
5. Checklist :
   - [ ] Créer TokenResponse et UserLogin
"""

from pydantic import BaseModel

# class UserLogin(BaseModel):
#     pass
