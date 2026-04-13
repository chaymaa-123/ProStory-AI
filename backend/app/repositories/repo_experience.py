from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional
from ..modeles.experience_modele import Experience
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate


class RepositoryExperience:
    """Repository pour les opérations DB des expériences"""
    
    @staticmethod
    def creer_experience(db: Session, experience_data: ExperienceCreate, utilisateur_id: int) -> Experience:
        """Crée une nouvelle expérience"""
        db_experience = Experience(
            utilisateur_id=utilisateur_id,
            titre=experience_data.titre,
            contenu=experience_data.contenu,
            tags=experience_data.tags,
            domaine_activite=experience_data.domaine_activite
        )
        db.add(db_experience)
        db.commit()
        db.refresh(db_experience)
        return db_experience
    
    @staticmethod
    def obtenir_par_id(db: Session, experience_id: int) -> Optional[Experience]:
        """Récupère une expérience par ID"""
        return db.query(Experience).filter(Experience.id == experience_id).first()
    
    @staticmethod
    def obtenir_par_utilisateur(db: Session, utilisateur_id: int, skip: int = 0, limit: int = 10) -> List[Experience]:
        """Récupère les expériences d'un utilisateur"""
        return db.query(Experience).filter(
            Experience.utilisateur_id == utilisateur_id
        ).order_by(desc(Experience.date_creation)).offset(skip).limit(limit).all()
    
    @staticmethod
    def obtenir_tous(db: Session, skip: int = 0, limit: int = 20) -> List[Experience]:
        """Récupère toutes les expériences"""
        return db.query(Experience).order_by(desc(Experience.date_creation)).offset(skip).limit(limit).all()
    
    @staticmethod
    def mettre_a_jour(db: Session, experience_id: int, experience_data: ExperienceUpdate) -> Optional[Experience]:
        """Met à jour une expérience"""
        db_experience = db.query(Experience).filter(Experience.id == experience_id).first()
        if not db_experience:
            return None
        
        if experience_data.titre is not None:
            db_experience.titre = experience_data.titre
        if experience_data.contenu is not None:
            db_experience.contenu = experience_data.contenu
        if experience_data.tags is not None:
            db_experience.tags = experience_data.tags
        if experience_data.domaine_activite is not None:
            db_experience.domaine_activite = experience_data.domaine_activite
        
        db.commit()
        db.refresh(db_experience)
        return db_experience
    
    @staticmethod
    def supprimer(db: Session, experience_id: int) -> bool:
        """Supprime une expérience"""
        db_experience = db.query(Experience).filter(Experience.id == experience_id).first()
        if not db_experience:
            return False
        
        db.delete(db_experience)
        db.commit()
        return True
