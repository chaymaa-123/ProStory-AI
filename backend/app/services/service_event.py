from typing import List, Optional
from uuid import UUID
from ..repositories.repo_event import RepositoryEvent
from ..schemas.event_schema import EventCreate, EventUpdate, EventResponse, EventListResponse

class ServiceEvent:
    @staticmethod
    def creer_event(event_data: EventCreate, creator_id: str) -> EventResponse:
        db_event = RepositoryEvent.creer_event(event_data, creator_id)
        return EventResponse(**db_event)

    @staticmethod
    def obtenir_event(event_id: str) -> Optional[EventResponse]:
        db_event = RepositoryEvent.obtenir_par_id(event_id)
        if not db_event:
            return None
        return EventResponse(**db_event)

    @staticmethod
    def obtenir_tous(skip: int = 0, limit: int = 20) -> List[EventListResponse]:
        db_events = RepositoryEvent.obtenir_tous(skip, limit)
        return [EventListResponse(**event) for event in db_events]

    @staticmethod
    def obtenir_events_utilisateur(creator_id: str, skip: int = 0, limit: int = 20) -> List[EventListResponse]:
        db_events = RepositoryEvent.obtenir_par_utilisateur(creator_id, skip, limit)
        return [EventListResponse(**event) for event in db_events]

    @staticmethod
    def obtenir_events_entreprise(company_id: str, skip: int = 0, limit: int = 20) -> List[EventListResponse]:
        db_events = RepositoryEvent.obtenir_par_entreprise(company_id, skip, limit)
        return [EventListResponse(**event) for event in db_events]

    @staticmethod
    def mettre_a_jour_event(event_id: str, event_update: EventUpdate, creator_id: str) -> Optional[EventResponse]:
        # Vérifier que l'événement existe et appartient au créateur
        existing_event = RepositoryEvent.obtenir_par_id(event_id)
        if not existing_event or existing_event["creator_id"] != creator_id:
            return None
            
        updated_event = RepositoryEvent.mettre_a_jour(event_id, event_update)
        if not updated_event:
            return None
        return EventResponse(**updated_event)

    @staticmethod
    def supprimer_event(event_id: str, creator_id: str) -> bool:
        # Vérifier que l'événement existe et appartient au créateur
        existing_event = RepositoryEvent.obtenir_par_id(event_id)
        if not existing_event or existing_event["creator_id"] != creator_id:
            return False
            
        return RepositoryEvent.supprimer(event_id)

    @staticmethod
    def rechercher_events(query: str, skip: int = 0, limit: int = 20) -> List[EventListResponse]:
        db_events = RepositoryEvent.rechercher(query, skip, limit)
        return [EventListResponse(**event) for event in db_events]

    @staticmethod
    def obtenir_events_par_categorie(category: str, skip: int = 0, limit: int = 20) -> List[EventListResponse]:
        db_events = RepositoryEvent.obtenir_par_categorie(category, skip, limit)
        return [EventListResponse(**event) for event in db_events]

    @staticmethod
    def obtenir_evenements_a_venir(skip: int = 0, limit: int = 20) -> List[EventListResponse]:
        db_events = RepositoryEvent.obtenir_evenements_a_venir(skip, limit)
        return [EventListResponse(**event) for event in db_events]
