from typing import List, Optional, Dict, Any
from ..coeur.base_de_donnees import supabase
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate


class RepositoryExperience:
    """Repository pour les opérations DB des expériences via Supabase"""

    TABLE_NAME = "experiences"

    @staticmethod
    def creer_experience(experience_data: ExperienceCreate, utilisateur_id: int) -> Dict[str, Any]:
        """Crée une nouvelle expérience"""
        data = {
            "utilisateur_id": utilisateur_id,
            "titre": experience_data.titre,
            "contenu": experience_data.contenu,
            "tags": experience_data.tags,
            "domaine_activite": experience_data.domaine_activite,
        }
        response = supabase.table(RepositoryExperience.TABLE_NAME).insert(data).execute()
        if response.data:
            return response.data[0]
        raise Exception("Erreur lors de la création de l'expérience")

    @staticmethod
    def obtenir_par_id(experience_id: int) -> Optional[Dict[str, Any]]:
        """Récupère une expérience par ID"""
        response = supabase.table(RepositoryExperience.TABLE_NAME).select("*").eq("id", experience_id).execute()
        if response.data:
            return response.data[0]
        return None

    @staticmethod
    def obtenir_par_utilisateur(utilisateur_id: int, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
        """Récupère les expériences d'un utilisateur"""
        response = (
            supabase.table(RepositoryExperience.TABLE_NAME)
            .select("*")
            .eq("utilisateur_id", utilisateur_id)
            .order("date_creation", desc=True)
            .range(skip, skip + limit - 1)
            .execute()
        )
        return response.data if response.data else []

    @staticmethod
    def obtenir_tous(skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère toutes les expériences"""
        response = (
            supabase.table(RepositoryExperience.TABLE_NAME)
            .select("*")
            .order("date_creation", desc=True)
            .range(skip, skip + limit - 1)
            .execute()
        )
        return response.data if response.data else []

    @staticmethod
    def mettre_a_jour(experience_id: int, experience_data: ExperienceUpdate) -> Optional[Dict[str, Any]]:
        """Met à jour une expérience"""
        update_data = {}

        if experience_data.titre is not None:
            update_data["titre"] = experience_data.titre
        if experience_data.contenu is not None:
            update_data["contenu"] = experience_data.contenu
        if experience_data.tags is not None:
            update_data["tags"] = experience_data.tags
        if experience_data.domaine_activite is not None:
            update_data["domaine_activite"] = experience_data.domaine_activite

        if not update_data:
            return RepositoryExperience.obtenir_par_id(experience_id)

        response = (
            supabase.table(RepositoryExperience.TABLE_NAME)
            .update(update_data)
            .eq("id", experience_id)
            .execute()
        )
        if response.data:
            return response.data[0]
        return None

    @staticmethod
    def supprimer(experience_id: int) -> bool:
        """Supprime une expérience"""
        response = (
            supabase.table(RepositoryExperience.TABLE_NAME)
            .delete()
            .eq("id", experience_id)
            .execute()
        )
        return response.status_code == 204 or (response.data and len(response.data) > 0)
