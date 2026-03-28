"""
FICHIER : utilisateur_modele.py
OBJECTIF : Schéma de la table de base de données pour les Utilisateurs.
CE QU'IL FAUT FAIRE ICI :
1. Ajouter les colonnes manquantes (ex: nom, prenom, bio, avatars).
2. Créer la relation `experiences = relationship(...)` pour lier un utilisateur à ses posts.
"""

"""
1. Objectif : Mapping objet-relationnel (ORM) de la table utilisateur.
2. Contenu prévu : Classe Utilisateur avec colonnes SQLAlchemy.
3. Responsable : Backend.
4. Interactions : Lu par les repositories.
5. Checklist :
   - [ ] Définir email, mot_de_passe_hash, role
"""

from sqlalchemy import Column, Integer
from ..coeur.base_de_donnees import Base

# class Utilisateur(Base):
#     __tablename__ = 'utilisateurs'
#     id = Column(Integer, primary_key=True, index=True)
