"""
FICHIER : service_experience.py
OBJECTIF : Logique métier (Business Logic) pour les expériences.
CE QU'IL FAUT FAIRE ICI :
1. Avant de sauvegarder, appeler `generer_embedding` pour vectoriser le contenu.
2. Gérer les erreurs proprement (ex: si l'IA de filtrage échoue).
"""

"""
1. Objectif : Orchestrer IA, Database et Règles Métier.
2. Contenu prévu : Workflow de publication (Filtrer -> Score -> Embedding -> DB).
3. Responsable : Backend.
4. Interactions : Appelle ia/, repositories/, appelé par routes/.
5. Checklist :
   - [ ] Coder publier_nouvelle_experience()
"""

# Fonctions de logique metier
