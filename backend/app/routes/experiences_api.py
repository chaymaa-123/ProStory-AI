"""Routes API pour les expériences - CRUD complet"""

from fastapi import APIRouter, HTTPException, status, Query, Header
from typing import List, Optional
from uuid import UUID
from ..services.service_experience import ServiceExperience
from ..repositories.repo_insight import RepositoryInsight
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate, ExperienceResponse, ExperienceListResponse
from ..schemas.insight_schema import ExperienceInsightResponse

router = APIRouter(prefix="/api/experience", tags=["experiences"])


@router.post("/", response_model=ExperienceResponse, status_code=status.HTTP_201_CREATED)
def creer_experience(
    experience: ExperienceCreate,
    user_id: str = Header(..., alias="x_user_id")
):
    """Créer une nouvelle expérience"""
    return ServiceExperience.creer_experience(experience, user_id)


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
    user_id: str = Header(..., alias="x_user_id")
):
    """Récupérer mes expériences"""
    return ServiceExperience.obtenir_mes_experiences(user_id, skip, limit)


@router.get("/{experience_id}", response_model=ExperienceResponse)
def obtenir_experience(
    experience_id: str
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
    experience_id: str,
    experience_update: ExperienceUpdate,
    user_id: str = Header(..., alias="x_user_id")
):
    """Mettre à jour une expérience"""
    updated_experience = ServiceExperience.mettre_a_jour_experience(experience_id, experience_update, user_id)
    if not updated_experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expérience non trouvée ou accès refusé"
        )
    return updated_experience


@router.delete("/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_experience(
    experience_id: str,
    user_id: str = Header(..., alias="x_user_id")
):
    """Supprimer une expérience"""
    experience = ServiceExperience.obtenir_experience(experience_id)
    if not experience:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expérience non trouvée")
    
    if experience.user_id != UUID(user_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Non autorisé")
    
    ServiceExperience.supprimer_experience(experience_id)


@router.get("/{experience_id}/insights", response_model=ExperienceInsightResponse)
def obtenir_insights_experience(
    experience_id: str
):
    """Récupérer les insights IA d'une expérience"""
    # Vérifier que l'expérience existe
    experience = ServiceExperience.obtenir_experience(experience_id)
    if not experience:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expérience non trouvée")
    
    # Récupérer l'insight
    insight = RepositoryInsight.obtenir_par_experience(experience_id)
    if not insight:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Insight non trouvé")
    
    # Formatter la réponse
    sentiment_labels = {
        "positif": "Positif",
        "neutre": "Neutre", 
        "negatif": "Négatif"
    }
    
    sentiment_colors = {
        "positif": "green",
        "neutre": "gray",
        "negatif": "red"
    }
    
    return ExperienceInsightResponse(
        experience_id=insight["experience_id"],
        sentiment=insight["sentiment"],
        keywords=insight["keywords"],
        score=insight["score"],
        confidence=insight["score"],  # Utiliser le score comme confiance
        created_at=insight["created_at"],
        sentiment_label=sentiment_labels.get(insight["sentiment"], insight["sentiment"]),
        sentiment_color=sentiment_colors.get(insight["sentiment"], "gray")
    )
