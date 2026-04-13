from sqlalchemy.orm import Session
from typing import List, Optional
from ..repositories.repo_experience import RepositoryExperience
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate, ExperienceResponse, ExperienceListResponse


class ServiceExperience:
    """Service métier pour les expériences"""
    
    @staticmethod
    def creer_experience(db: Session, experience_data: ExperienceCreate, utilisateur_id: int) -> ExperienceResponse:
        """Crée une nouvelle expérience"""
        db_experience = RepositoryExperience.creer_experience(db, experience_data, utilisateur_id)
        return ExperienceResponse.from_orm(db_experience)
    
    @staticmethod
    def obtenir_experience(db: Session, experience_id: int) -> Optional[ExperienceResponse]:
        """Récupère une expérience par ID"""
        db_experience = RepositoryExperience.obtenir_par_id(db, experience_id)
        if not db_experience:
            return None
        return ExperienceResponse.from_orm(db_experience)
    
    @staticmethod
    def obtenir_mes_experiences(db: Session, utilisateur_id: int, skip: int = 0, limit: int = 10) -> List[ExperienceListResponse]:
        """Récupère mes expériences"""
        experiences = RepositoryExperience.obtenir_par_utilisateur(db, utilisateur_id, skip, limit)
        return [ExperienceListResponse.from_orm(exp) for exp in experiences]
    
    @staticmethod
    def obtenir_feed(db: Session, skip: int = 0, limit: int = 20) -> List[ExperienceListResponse]:
        """Récupère le feed"""
        experiences = RepositoryExperience.obtenir_tous(db, skip, limit)
        return [ExperienceListResponse.from_orm(exp) for exp in experiences]
    
    @staticmethod
    def mettre_a_jour_experience(db: Session, experience_id: int, experience_data: ExperienceUpdate, utilisateur_id: int) -> Optional[ExperienceResponse]:
        """Met à jour une expérience"""
        db_experience = RepositoryExperience.obtenir_par_id(db, experience_id)
        if not db_experience or db_experience.utilisateur_id != utilisateur_id:
            return None
        
        updated_experience = RepositoryExperience.mettre_a_jour(db, experience_id, experience_data)
        return ExperienceResponse.from_orm(updated_experience) if updated_experience else None
    
    @staticmethod
    def supprimer_experience(db: Session, experience_id: int, utilisateur_id: int) -> bool:
        """Supprime une expérience"""
        db_experience = RepositoryExperience.obtenir_par_id(db, experience_id)
        if not db_experience or db_experience.utilisateur_id != utilisateur_id:
            return False
        
        return RepositoryExperience.supprimer(db, experience_id)
