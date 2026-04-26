from typing import List, Optional, Dict, Any
from uuid import UUID
from ..coeur.base_de_donnees import supabase
from ..schemas.experience_schema import ExperienceCreate, ExperienceUpdate

class RepositoryExperience:
    """
    Repository pour la gestion des expériences professionnelles.
    Gère les relations complexes avec les tables de jointure (tags, entreprises, événements).
    """
    
    EXPERIENCES_TABLE = "experiences"
    TAGS_TABLE = "tags"
    EXPERIENCE_TAGS_TABLE = "experience_tags"
    EXPERIENCE_COMPANY_TABLE = "experience_company"
    EXPERIENCE_EVENT_TABLE = "experience_event"

    @staticmethod
    def creer_experience(experience_data: ExperienceCreate, user_id: str) -> Dict[str, Any]:
        """
        Crée une nouvelle expérience et gère automatiquement les liaisons 
        avec l'entreprise (get_or_create) et les tags.
        """
        # 1. Insertion dans la table principale 'experiences'
        experience_dict = {
            "user_id": user_id,
            "title": experience_data.title,
            "content": experience_data.content,
            "category": experience_data.category,
        }
        
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE).insert(experience_dict).execute()
        if not response.data:
            raise Exception("Erreur lors de la création de l'expérience en base de données.")
        
        experience = response.data[0]
        exp_id = experience['id']

        # 2. Liaison Entreprise (Mécanisme Automatique)
        if experience_data.company_id:
            company_id = RepositoryExperience._get_or_create_company(experience_data.company_id)
            if company_id:
                supabase.table(RepositoryExperience.EXPERIENCE_COMPANY_TABLE).insert({
                    "experience_id": exp_id,
                    "company_id": company_id
                }).execute()

        # 3. Liaison Événement
        if experience_data.event_id:
            supabase.table(RepositoryExperience.EXPERIENCE_EVENT_TABLE).insert({
                "experience_id": exp_id,
                "event_id": experience_data.event_id
            }).execute()

        # 4. Liaison Tags
        if experience_data.tags:
            RepositoryExperience._handle_tags_for_experience(exp_id, experience_data.tags)

        return RepositoryExperience.obtenir_par_id(exp_id)

    @staticmethod
    def _get_or_create_company(company_id_or_name: str) -> Optional[str]:
        """
        Résout un ID d'entreprise ou récupère une entreprise existante par son nom.
        Crée une nouvelle entrée uniquement si elle n'existe vraiment pas.
        """
        if not company_id_or_name:
            return None
            
        # 1. Tenter de valider comme UUID (si l'utilisateur a sélectionné une entreprise existante)
        try:
            UUID(company_id_or_name)
            return company_id_or_name
        except ValueError:
            # Ce n'est pas un UUID, donc c'est un nom saisi manuellement
            clean_name = company_id_or_name.strip()
            
            # 2. Recherche par nom exact (insensible à la casse avec ilike)
            response = supabase.table("companies")\
                .select("id")\
                .ilike("name", clean_name)\
                .execute()
            
            if response.data and len(response.data) > 0:
                # L'entreprise existe déjà, on retourne son ID
                return response.data[0]["id"]
            
            # 3. Création automatique si vraiment introuvable
            try:
                create_resp = supabase.table("companies")\
                    .insert({"name": clean_name})\
                    .execute()
                
                if create_resp.data:
                    return create_resp.data[0]["id"]
            except Exception as e:
                # En cas d'erreur (ex: violation de contrainte unique si elle existe)
                # On retente une dernière fois la recherche
                final_check = supabase.table("companies").select("id").ilike("name", clean_name).execute()
                if final_check.data:
                    return final_check.data[0]["id"]
            
            return None


    @staticmethod
    def _handle_tags_for_experience(experience_id: str, tags: List[str]):
        """Gère l'insertion et la liaison des tags pour une expérience."""
        for tag_name in tags:
            tag_name = tag_name.strip()
            # Upsert du tag
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
                
            # Liaison Junction
            supabase.table(RepositoryExperience.EXPERIENCE_TAGS_TABLE)\
                .insert({"experience_id": experience_id, "tag_id": tag_id})\
                .execute()

    @staticmethod
    def obtenir_par_id(experience_id: str) -> Optional[Dict[str, Any]]:
        """Récupère une expérience avec toutes ses relations formatées."""
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .select("*, author:users!experiences_user_id_fkey(name), tags:experience_tags(tag:tags(name)), companies:experience_company(company:companies(id, name)), events:experience_event(event:events(title))")\
            .eq("id", experience_id)\
            .single()\
            .execute()
            
        return RepositoryExperience._format_single_experience(response.data) if response.data else None

    @staticmethod
    def obtenir_par_utilisateur(user_id: str, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
        """Récupère les expériences d'un utilisateur spécifique."""
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .select("*, author:users!experiences_user_id_fkey(name), tags:experience_tags(tag:tags(name)), companies:experience_company(company:companies(id, name)), events:experience_event(event:events(title))")\
            .eq("user_id", user_id)\
            .order("created_at", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
        return [RepositoryExperience._format_single_experience(exp) for exp in (response.data or [])]

    @staticmethod
    def obtenir_tous(skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère le flux global des expériences."""
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
            .select("*, author:users!experiences_user_id_fkey(name), tags:experience_tags(tag:tags(name)), companies:experience_company(company:companies(id, name)), events:experience_event(event:events(title))")\
            .order("created_at", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
        return [RepositoryExperience._format_single_experience(exp) for exp in (response.data or [])]

    @staticmethod
    def _format_single_experience(exp: Dict[str, Any]) -> Dict[str, Any]:
        """Aplatit les relations Supabase complexes vers un format JSON simple pour le frontend."""
        # Extraction des tags
        if "tags" in exp:
            exp["tags"] = [t["tag"]["name"] for t in exp["tags"] if t.get("tag")]
        
        # Extraction de l'entreprise
        if "companies" in exp and exp["companies"]:
            company_data = exp["companies"][0].get("company")
            if company_data:
                exp["company_id"] = company_data.get("id")
                exp["company_name"] = company_data.get("name")
            del exp["companies"]
        
        # Extraction de l'événement
        if "events" in exp and exp["events"]:
            event_data = exp["events"][0].get("event")
            if event_data:
                exp["event_name"] = event_data.get("title")
            del exp["events"]
        
        # Extraction de l'auteur
        if "author" in exp and exp["author"]:
            exp["author_name"] = exp["author"].get("name", "Anonyme")
            del exp["author"]
        
        return exp

    @staticmethod
    def mettre_a_jour(experience_id: str, experience_data: ExperienceUpdate) -> Optional[Dict[str, Any]]:
        """Met à jour une expérience et ses relations."""
        update_data = {}
        if experience_data.title is not None: update_data["title"] = experience_data.title
        if experience_data.content is not None: update_data["content"] = experience_data.content
        if experience_data.category is not None: update_data["category"] = experience_data.category

        if update_data:
            supabase.table(RepositoryExperience.EXPERIENCES_TABLE)\
                .update(update_data).eq("id", experience_id).execute()

        # Update Entreprise
        if experience_data.company_id is not None:
            supabase.table(RepositoryExperience.EXPERIENCE_COMPANY_TABLE).delete().eq("experience_id", experience_id).execute()
            company_id = RepositoryExperience._get_or_create_company(experience_data.company_id)
            if company_id:
                supabase.table(RepositoryExperience.EXPERIENCE_COMPANY_TABLE).insert({"experience_id": experience_id, "company_id": company_id}).execute()

        # Mise à jour Événement
        if experience_data.event_id is not None:
            supabase.table(RepositoryExperience.EXPERIENCE_EVENT_TABLE).delete().eq("experience_id", experience_id).execute()
            if experience_data.event_id:
                supabase.table(RepositoryExperience.EXPERIENCE_EVENT_TABLE).insert({"experience_id": experience_id, "event_id": experience_data.event_id}).execute()

        # Update Tags
        if experience_data.tags is not None:
            supabase.table(RepositoryExperience.EXPERIENCE_TAGS_TABLE).delete().eq("experience_id", experience_id).execute()
            RepositoryExperience._handle_tags_for_experience(experience_id, experience_data.tags)

        return RepositoryExperience.obtenir_par_id(experience_id)

    @staticmethod
    def supprimer(experience_id: str) -> bool:
        """Supprime une expérience et nettoie les tables de jointure."""
        supabase.table(RepositoryExperience.EXPERIENCE_COMPANY_TABLE).delete().eq("experience_id", experience_id).execute()
        supabase.table(RepositoryExperience.EXPERIENCE_EVENT_TABLE).delete().eq("experience_id", experience_id).execute()
        supabase.table(RepositoryExperience.EXPERIENCE_TAGS_TABLE).delete().eq("experience_id", experience_id).execute()
        
        response = supabase.table(RepositoryExperience.EXPERIENCES_TABLE).delete().eq("id", experience_id).execute()
        return len(response.data) > 0 or response.count > 0

