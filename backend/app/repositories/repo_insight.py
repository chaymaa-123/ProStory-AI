from typing import List, Optional, Dict, Any
from ..coeur.base_de_donnees import supabase
from ..schemas.insight_schema import InsightCreate, InsightUpdate

class RepositoryInsight:
    INSIGHTS_TABLE = "insights"

    @staticmethod
    def creer_insight(insight_data: InsightCreate) -> Dict[str, Any]:
        """Crée un nouvel insight pour une expérience"""
        insight_dict = {
            "experience_id": insight_data.experience_id,
            "sentiment": insight_data.sentiment,
            "keywords": insight_data.keywords,
            "score": insight_data.score
        }
        
        response = supabase.table(RepositoryInsight.INSIGHTS_TABLE).insert(insight_dict).execute()
        
        if not response.data:
            raise Exception("Erreur création insight")
            
        return response.data[0]

    @staticmethod
    def obtenir_par_experience(experience_id: str) -> Optional[Dict[str, Any]]:
        """Récupère l'insight d'une expérience"""
        response = supabase.table(RepositoryInsight.INSIGHTS_TABLE)\
            .select("*")\
            .eq("experience_id", experience_id)\
            .single()\
            .execute()
            
        if response.data:
            return response.data
        return None

    @staticmethod
    def obtenir_tous(skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Récupère tous les insights avec pagination"""
        response = supabase.table(RepositoryInsight.INSIGHTS_TABLE)\
            .select("*")\
            .order("created_at", desc=True)\
            .range(skip, skip + limit - 1)\
            .execute()
            
        return response.data or []

    @staticmethod
    def mettre_a_jour(insight_id: str, insight_data: InsightUpdate) -> Optional[Dict[str, Any]]:
        """Met à jour un insight"""
        update_data = {}
        
        if insight_data.sentiment is not None:
            update_data["sentiment"] = insight_data.sentiment
        if insight_data.keywords is not None:
            update_data["keywords"] = insight_data.keywords
        if insight_data.score is not None:
            update_data["score"] = insight_data.score
            
        if not update_data:
            return RepositoryInsight.obtenir_par_id(insight_id)
            
        response = supabase.table(RepositoryInsight.INSIGHTS_TABLE)\
            .update(update_data)\
            .eq("id", insight_id)\
            .execute()
            
        if response.data:
            return response.data[0]
        return None

    @staticmethod
    def obtenir_par_id(insight_id: str) -> Optional[Dict[str, Any]]:
        """Récupère un insight par son ID"""
        response = supabase.table(RepositoryInsight.INSIGHTS_TABLE)\
            .select("*")\
            .eq("id", insight_id)\
            .single()\
            .execute()
            
        if response.data:
            return response.data
        return None

    @staticmethod
    def supprimer(insight_id: str) -> bool:
        """Supprime un insight"""
        response = supabase.table(RepositoryInsight.INSIGHTS_TABLE)\
            .delete()\
            .eq("id", insight_id)\
            .execute()
            
        return len(response.data) > 0

    @staticmethod
    def obtenir_statistiques_sentiments() -> Dict[str, Any]:
        """Calcule les statistiques des sentiments"""
        response = supabase.table(RepositoryInsight.INSIGHTS_TABLE)\
            .select("sentiment")\
            .execute()
            
        if not response.data:
            return {
                "total": 0,
                "positif": 0,
                "neutre": 0,
                "negatif": 0,
                "pourcentages": {
                    "positif": 0.0,
                    "neutre": 0.0,
                    "negatif": 0.0
                }
            }
            
        sentiments = [item["sentiment"] for item in response.data]
        total = len(sentiments)
        
        stats = {
            "total": total,
            "positif": sentiments.count("positif"),
            "neutre": sentiments.count("neutre"),
            "negatif": sentiments.count("negatif"),
            "pourcentages": {}
        }
        
        if total > 0:
            stats["pourcentages"] = {
                "positif": round(stats["positif"] / total * 100, 1),
                "neutre": round(stats["neutre"] / total * 100, 1),
                "negatif": round(stats["negatif"] / total * 100, 1)
            }
            
        return stats
