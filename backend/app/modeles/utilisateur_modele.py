from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from ..coeur.base_de_donnees import Base
from datetime import datetime


class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100))
    bio = Column(Text)
    avatar_url = Column(String(500))
    role = Column(String(20), default='user')
    date_creation = Column(DateTime, default=datetime.utcnow)
    date_modification = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relation avec les expériences
    experiences = relationship("Experience", back_populates="utilisateur", cascade="all, delete-orphan")
