"""
FICHIER : experience_modele.py
OBJECTIF : Schéma de la table de base de données pour les Expériences (Posts).
CE QU'IL FAUT FAIRE ICI :
1. Décommenter et configurer la colonne `embedding` avec `pgvector`.
2. Ajouter des champs supplémentaires (ex: domaine_activite, mots_cles, date_publication).
"""

"""
1. Objectif : Mapping ORM de la table expérience.
2. Contenu prévu : Titre, contenu, score_ia, statut_validation, embedding.
3. Responsable : Backend / IA.
4. Interactions : Relation avec Utilisateur et Tags.
5. Checklist :
   - [ ] Définir la colonne embedding = Column(Vector(384))
"""

from sqlalchemy import Column, Integer
from ..coeur.base_de_donnees import Base

# class Experience(Base):
#     __tablename__ = 'experiences'
#     id = Column(Integer, primary_key=True, index=True)
