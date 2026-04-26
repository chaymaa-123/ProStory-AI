from typing import List, Optional, Dict, Any
from ..coeur.base_de_donnees import supabase
from ..schemas.event_schema import EventCreate, EventUpdate

class RepositoryEvent:
    EVENTS_TABLE = "events"

    @staticmethod
    def creer_event(event_data: EventCreate, creator_id: str) -> Dict[str, Any]:
        """Crée un nouvel événement"""
        event_dict = {
            "title": event_data.title,
            "description": event_data.description,
            "date": event_data.date.isoformat(),
            "location": event_data.location,
            "category": event_data.category,
            "is_virtual": event_data.is_virtual,
            "max_attendees": event_data.max_attendees,
            "creator_id": creator_id,
            "company_id": str(event_data.company_id) if event_data.company_id else None
        }
        
        response = supabase.table(RepositoryEvent.EVENTS_TABLE).insert(event_dict).execute()
        
        if not response.data:
            raise Exception("Erreur création événement")
            
        return response.data[0]

    @staticmethod
    def obtenir_par_id(event_id: str) -> Optional[Dict[str, Any]]:
        """Récupère un événement par son ID"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .select("*")\
            .eq("id", event_id)\
            .single()\
            .execute()
            
        if response.data:
            return response.data
        return None

    @staticmethod
    def obtenir_tous(skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère tous les événements avec pagination"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .select("*")\
            .order("date", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
            
        return response.data or []

    @staticmethod
    def obtenir_par_utilisateur(creator_id: str, skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère les événements créés par un utilisateur"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .select("*")\
            .eq("creator_id", creator_id)\
            .order("date", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
            
        return response.data or []

    @staticmethod
    def obtenir_par_entreprise(company_id: str, skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère les événements d'une entreprise"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .select("*")\
            .eq("company_id", company_id)\
            .order("date", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
            
        return response.data or []

    @staticmethod
    def mettre_a_jour(event_id: str, event_data: EventUpdate) -> Optional[Dict[str, Any]]:
        """Met à jour un événement"""
        update_data = {}
        
        if event_data.title is not None:
            update_data["title"] = event_data.title
        if event_data.description is not None:
            update_data["description"] = event_data.description
        if event_data.date is not None:
            update_data["date"] = event_data.date.isoformat()
        if event_data.location is not None:
            update_data["location"] = event_data.location
        if event_data.category is not None:
            update_data["category"] = event_data.category
        if event_data.is_virtual is not None:
            update_data["is_virtual"] = event_data.is_virtual
        if event_data.max_attendees is not None:
            update_data["max_attendees"] = event_data.max_attendees
            
        if not update_data:
            return RepositoryEvent.obtenir_par_id(event_id)
            
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .update(update_data)\
            .eq("id", event_id)\
            .execute()
            
        if response.data:
            return response.data[0]
        return None

    @staticmethod
    def supprimer(event_id: str) -> bool:
        """Supprime un événement"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .delete()\
            .eq("id", event_id)\
            .execute()
            
        return len(response.data) > 0

    @staticmethod
    def rechercher(query: str, skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Recherche des événements par titre ou description"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .select("*")\
            .or(f"title.ilike.%{query}%,description.ilike.%{query}%")\
            .order("date", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
            
        return response.data or []

    @staticmethod
    def obtenir_par_categorie(category: str, skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère les événements par catégorie"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .select("*")\
            .eq("category", category)\
            .order("date", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
            
        return response.data or []

    @staticmethod
    def obtenir_evenements_a_venir(skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère les événements à venir"""
        response = supabase.table(RepositoryEvent.EVENTS_TABLE)\
            .select("*")\
            .gte("date", "now()")\
            .order("date", asc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
            
        return response.data or []
