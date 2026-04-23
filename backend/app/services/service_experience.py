from typing import List, Optional
from uuid import UUID
from ..repositories.repo_experience import RepositoryExperience
from ..repositories.repo_insight import RepositoryInsight
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate, ExperienceResponse, ExperienceListResponse
from ..schemas.insight_schema import InsightCreate
from ..recommendations import analyze_text
import logging

logger = logging.getLogger(__name__)

class ServiceExperience:
    @staticmethod
    def creer_experience(experience_data: ExperienceCreate, user_id: str) -> ExperienceResponse:
        # Création de l'expérience
        db_experience = RepositoryExperience.creer_experience(experience_data, user_id)
        
        # Analyse IA du contenu
        try:
            analysis_result = analyze_text(experience_data.content)
            
            # Création de l'insight
            insight_data = InsightCreate(
                experience_id=db_experience['id'],
                sentiment=analysis_result['sentiment'],
                keywords=analysis_result['keywords'],
                score=analysis_result['confidence']
            )
            
            RepositoryInsight.creer_insight(insight_data)
            logger.info(f"Insight créé pour l'expérience {db_experience['id']}")
            
        except Exception as e:
            logger.error(f"Erreur lors de la création de l'insight: {e}")
            # On continue même si l'analyse IA échoue
        
        return ExperienceResponse(**db_experience)

    @staticmethod
    def obtenir_experience(experience_id: str) -> Optional[ExperienceResponse]:
        db_experience = RepositoryExperience.obtenir_par_id(experience_id)
        if not db_experience:
            return None
        return ExperienceResponse(**db_experience)

    @staticmethod
    def obtenir_mes_experiences(user_id: str, skip: int = 0, limit: int = 10) -> List[ExperienceListResponse]:
        experiences = RepositoryExperience.obtenir_par_utilisateur(user_id, skip, limit)
        return [ExperienceListResponse(**exp) for exp in experiences]

    @staticmethod
    def obtenir_feed(skip: int = 0, limit: int = 20) -> List[ExperienceListResponse]:
        experiences = RepositoryExperience.obtenir_tous(skip, limit)
        return [ExperienceListResponse(**exp) for exp in experiences]

    @staticmethod
    def mettre_a_jour_experience(experience_id: str, experience_data: ExperienceUpdate, user_id: str) -> Optional[ExperienceResponse]:
        db_experience = RepositoryExperience.obtenir_par_id(experience_id)
        if not db_experience or db_experience.get("user_id") != user_id:
            return None
        updated_experience = RepositoryExperience.mettre_a_jour(experience_id, experience_data)
        return ExperienceResponse(**updated_experience) if updated_experience else None

    @staticmethod
    def supprimer_experience(experience_id: str, user_id: str) -> bool:
        db_experience = RepositoryExperience.obtenir_par_id(experience_id)
        if not db_experience or db_experience.get("user_id") != user_id:
            return False
        return RepositoryExperience.supprimer(experience_id)

