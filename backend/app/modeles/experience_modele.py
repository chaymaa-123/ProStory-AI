from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import VECTOR
from ..coeur.base_de_donnees import Base
from datetime import datetime


class Experience(Base):
    __tablename__ = 'experiences'
    
    id = Column(Integer, primary_key=True, index=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id', ondelete='CASCADE'), nullable=False)
    titre = Column(String(255), nullable=False)
    contenu = Column(Text, nullable=False)
    tags = Column(String(255))
    domaine_activite = Column(String(100))
    sentiment = Column(String(20))
    score_qualite = Column(Float, default=0)
    embedding = Column(VECTOR(384))
    date_creation = Column(DateTime, default=datetime.utcnow)
    date_modification = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relation avec l'utilisateur
    utilisateur = relationship("Utilisateur", back_populates="experiences")
