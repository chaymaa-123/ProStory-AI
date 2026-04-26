"""Routes API pour les événements - CRUD complet"""

from fastapi import APIRouter, HTTPException, status, Query, Header
from typing import List, Optional
from uuid import UUID
from ..services.service_event import ServiceEvent
from ..schemas.event_schema import EventCreate, EventUpdate, EventResponse, EventListResponse

router = APIRouter(prefix="/api/events", tags=["events"])

@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def creer_event(
    event: EventCreate,
    user_id: str = Header(..., alias="x_user_id")
):
    """Créer un nouvel événement (utilisateur ou entreprise)"""
    return ServiceEvent.creer_event(event, user_id)

@router.get("/", response_model=List[EventListResponse])
def obtenir_tous_events(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    """Récupérer tous les événements"""
    return ServiceEvent.obtenir_tous(skip, limit)

@router.get("/upcoming", response_model=List[EventListResponse])
def obtenir_evenements_a_venir(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    """Récupérer les événements à venir"""
    return ServiceEvent.obtenir_evenements_a_venir(skip, limit)

@router.get("/my-events", response_model=List[EventListResponse])
def obtenir_mes_events(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    user_id: str = Header(..., alias="x_user_id")
):
    """Récupérer mes événements créés"""
    return ServiceEvent.obtenir_events_utilisateur(user_id, skip, limit)

@router.get("/company/{company_id}", response_model=List[EventListResponse])
def obtenir_events_entreprise(
    company_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    """Récupérer les événements d'une entreprise"""
    return ServiceEvent.obtenir_events_entreprise(company_id, skip, limit)

@router.get("/search", response_model=List[EventListResponse])
def rechercher_events(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    """Rechercher des événements"""
    return ServiceEvent.rechercher_events(q, skip, limit)

@router.get("/category/{category}", response_model=List[EventListResponse])
def obtenir_events_par_categorie(
    category: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    """Récupérer les événements par catégorie"""
    return ServiceEvent.obtenir_events_par_categorie(category, skip, limit)

@router.get("/{event_id}", response_model=EventResponse)
def obtenir_event(event_id: str):
    """Récupérer un événement par ID"""
    event = ServiceEvent.obtenir_event(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Événement non trouvé"
        )
    return event

@router.put("/{event_id}", response_model=EventResponse)
def mettre_a_jour_event(
    event_id: str,
    event_update: EventUpdate,
    user_id: str = Header(..., alias="x_user_id")
):
    """Mettre à jour un événement"""
    updated_event = ServiceEvent.mettre_a_jour_event(event_id, event_update, user_id)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Événement non trouvé ou accès refusé"
        )
    return updated_event

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_event(
    event_id: str,
    user_id: str = Header(..., alias="x_user_id")
):
    """Supprimer un événement"""
    success = ServiceEvent.supprimer_event(event_id, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Événement non trouvé ou accès refusé"
        )
