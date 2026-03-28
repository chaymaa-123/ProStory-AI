"""
1. Objectif : Outils pour les modérateurs.
2. Contenu prévu : Routes pour supprimer/valider les posts suspendus.
3. Responsable : Backend.
4. Interactions : Vérifie le rôle ADMIN du token.
5. Checklist :
   - [ ] Créer DELETE /admin/experience/{id}
"""

from fastapi import APIRouter

router = APIRouter()
