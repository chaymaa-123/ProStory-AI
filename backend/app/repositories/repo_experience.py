from typing import List, Optional, Dict, Any
from uuid import UUID, uuid4
from ..coeur.base_de_donnees import supabase
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate

class RepositoryExperience:
    EXPERIENCES_TABLE = "experiences"
    TAGS_TABLE = "tags"
    EXPERIENCE_TAGS_TABLE = "experience_tags"

    @staticmethod
    def creer_experience(experience_data: ExperienceCreate, user_id: str) -> Dict[str, Any]:
        experience_data_dict = {
            "user_id": user_id,
            "title": experience_data.title,
            "content": experience_data.content,
            "category": experience_data.category,
            "company_id": experience_data.company_id,
            "event_id": experience_data.event_id,
        }
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE).insert(experience_data_dict).execute()
        if not response.data:
            raise Exception("Erreur création expérience")
        experience = response.data[0]

        # Handle tags
        if experience_data.tags:
            RepositoryExperience._handle_tags_for_experience(experience['id'], experience_data.tags)

        return experience

    @staticmethod
    def _handle_tags_for_experience(experience_id: str, tags: List[str]):
        for tag_name in tags:
            # Upsert tag
            tag_response = supabase.table(RepositoryExperience.TAGS_TABLE)\
                .select("id")\
                .eq("name", tag_name)\
                .execute()
            if not tag_response.data:
                tag_insert = supabase.table(RepositoryExperience.TAGS_TABLE)\
                    .insert({"name": tag_name})\
                    .execute()
                tag_id = tag_insert.data[0]['id']
            else:
                tag_id = tag_response.data[0]['id']
            # Insert junction (ignore if exists)
            supabase.table(RepositoryExperience.EXPERIENCE_TAGS_TABLE)\
                .insert({
                    "experience_id": experience_id,
                    "tag_id": tag_id
                })\
                .execute()

    @staticmethod
    def obtenir_par_id(experience_id: str) -> Optional[Dict[str, Any]]:
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .select("*, tags!experience_tags_tag_id_fkey(name)")\
            .eq("id", experience_id)\
            .single()\
            .execute()
        if response.data:
            data = response.data
            data['tags'] = [tag['name'] for tag in data.get('tags', [])]
            return data
        return None

    @staticmethod
    def obtenir_par_utilisateur(user_id: str, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .select("*, tags!experience_tags_tag_id_fkey(name)")\
            .eq("user_id", user_id)\
            .order("created_at", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
        return RepositoryExperience._format_experiences(response.data)

    @staticmethod
    def obtenir_tous(skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .select("*, tags!experience_tags_tag_id_fkey(name)")\
            .order("created_at", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
        return RepositoryExperience._format_experiences(response.data)

    @staticmethod
    def _format_experiences(experiences: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for exp in experiences:
            exp['tags'] = [tag['name'] for tag in exp.get('tags', [])]
        return experiences

    @staticmethod
    def mettre_a_jour(experience_id: str, experience_data: ExperienceUpdate) -> Optional[Dict[str, Any]]:
        update_data = {}
        if experience_data.title is not None:
            update_data["title"] = experience_data.title
        if experience_data.content is not None:
            update_data["content"] = experience_data.content
        if experience_data.category is not None:
            update_data["category"] = experience_data.category
        if experience_data.company_id is not None:
            update_data["company_id"] = experience_data.company_id
        if experience_data.event_id is not None:
            update_data["event_id"] = experience_data.event_id

        if not update_data:
            return RepositoryExperience.obtenir_par_id(experience_id)

        supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .update(update_data)\
            .eq("id", experience_id)\
            .execute()

        if experience_data.tags is not None:
            supabase.table(RepositoryExperience.EXPERIENCE_TAGS_TABLE)\
                .delete()\
                .eq("experience_id", experience_id)\
                .execute()
            RepositoryExperience._handle_tags_for_experience(experience_id, experience_data.tags)

        return RepositoryExperience.obtenir_par_id(experience_id)

    @staticmethod
    def supprimer(experience_id: str) -> bool:
        supabase.table(RepositoryExperience.EXPERIENCE_TAGS_TABLE)\
            .delete()\
            .eq("experience_id", experience_id)\
            .execute()
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .delete()\
            .eq("id", experience_id)\
            .execute()
        return len(response.data) > 0 or response.count > 0

