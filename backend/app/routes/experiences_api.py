"""Routes API pour les expériences - CRUD complet"""

from fastapi import APIRouter, HTTPException, status, Query, Header
from typing import List, Optional

from ..services.service_experience import ServiceExperience
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate, ExperienceResponse, ExperienceListResponse

router = APIRouter(prefix="/api/experiences", tags=["experiences"])


def get_current_user_id(x_user_id: Optional[int] = Header(None)) -> int:
    """Récupère l'ID de l'utilisateur actuel du header"""
    if x_user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Utilisateur non authentifié"
        )
    return x_user_id


@router.post("/", response_model=ExperienceResponse, status_code=status.HTTP_201_CREATED)
def creer_experience(
    experience: ExperienceCreate,
    utilisateur_id: int = Header(..., alias="x_user_id")
):
    """Créer une nouvelle expérience"""
    return ServiceExperience.creer_experience(experience, utilisateur_id)


@router.get("/feed", response_model=List[ExperienceListResponse])
def obtenir_feed(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    """Récupérer le fil d'actualité"""
    return ServiceExperience.obtenir_feed(skip, limit)


@router.get("/mes-experiences", response_model=List[ExperienceListResponse])
def obtenir_mes_experiences(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    utilisateur_id: int = Header(..., alias="x_user_id")
):
    """Récupérer mes expériences"""
    return ServiceExperience.obtenir_mes_experiences(utilisateur_id, skip, limit)


@router.get("/{experience_id}", response_model=ExperienceResponse)
def obtenir_experience(
    experience_id: int
):
    """Récupérer une expérience par ID"""
    experience = ServiceExperience.obtenir_experience(experience_id)
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expérience non trouvée"
        )
    return experience


@router.put("/{experience_id}", response_model=ExperienceResponse)
def mettre_a_jour_experience(
    experience_id: int,
    experience_update: ExperienceUpdate,
    utilisateur_id: int = Header(..., alias="x_user_id")
):
    """Mettre à jour une expérience"""
    updated_experience = ServiceExperience.mettre_a_jour_experience(experience_id, experience_update, utilisateur_id)
    if not updated_experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expérience non trouvée ou accès refusé"
        )
    return updated_experience


@router.delete("/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_experience(
    experience_id: int,
    utilisateur_id: int = Header(..., alias="x_user_id")
):
    """Supprimer une expérience"""
    success = ServiceExperience.supprimer_experience(experience_id, utilisateur_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expérience non trouvée ou accès refusé"
        )
