from typing import List, Optional
from uuid import UUID
from ..repositories.repo_experience import RepositoryExperience
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate, ExperienceResponse, ExperienceListResponse

class ServiceExperience:
    @staticmethod
    def creer_experience(experience_data: ExperienceCreate, user_id: str) -> ExperienceResponse:
        db_experience = RepositoryExperience.creer_experience(experience_data, user_id)
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

