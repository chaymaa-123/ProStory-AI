"""Routes API pour les insights entreprise - Modèle économique viable"""

from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Any
from ..repositories.repo_insight import RepositoryInsight
from ..repositories.repo_experience import RepositoryExperience
from ..coeur.base_de_donnees import supabase
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/company", tags=["company-insights"])

@router.get("/{company_id}/insights")
def get_company_insights(company_id: str):
    """
    Récupère les insights agrégés pour une entreprise
    Endpoint principal du modèle économique
    """
    try:
        # Récupérer toutes les expériences de l'entreprise
        experiences_response = supabase.table("experiences")\
            .select("id, created_at")\
            .eq("company_id", company_id)\
            .execute()
        
        if not experiences_response.data:
            return {
                "company_id": company_id,
                "total_experiences": 0,
                "sentiment_distribution": {"positif": 0, "neutre": 0, "negatif": 0},
                "dominant_sentiment": "neutre",
                "keywords": [],
                "trend_data": [],
                "summary": "Aucune expérience disponible pour cette entreprise",
                "confidence": "Aucune donnée"
            }
        
        experience_ids = [exp["id"] for exp in experiences_response.data]
        
        # Récupérer tous les insights de ces expériences
        insights_response = supabase.table("insights")\
            .select("*")\
            .in_("experience_id", experience_ids)\
            .execute()
        
        insights = insights_response.data or []
        
        # Calculer les statistiques
        sentiment_counts = {"positif": 0, "neutre": 0, "negatif": 0}
        all_keywords = []
        
        for insight in insights:
            sentiment = insight["sentiment"]
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
            all_keywords.extend(insight.get("keywords", []))
        
        total = len(insights)
        dominant_sentiment = max(sentiment_counts, key=sentiment_counts.get) if total > 0 else "neutre"
        
        # Calculer les pourcentages
        if total > 0:
            sentiment_distribution = {
                "positif": round(sentiment_counts["positif"] / total * 100, 1),
                "neutre": round(sentiment_counts["neutre"] / total * 100, 1),
                "negatif": round(sentiment_counts["negatif"] / total * 100, 1)
            }
        else:
            sentiment_distribution = {"positif": 0, "neutre": 0, "negatif": 0}
        
        # Analyser les mots-clés les plus fréquents
        keyword_freq = {}
        for keyword in all_keywords:
            keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
        
        top_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Générer les tendances temporelles (mock pour l'instant)
        trend_data = generate_trend_data(insights)
        
        # Générer le résumé
        summary = generate_company_summary(sentiment_distribution, top_keywords, total)
        
        # Calculer la confiance
        confidence = calculate_confidence(total, sentiment_distribution)
        
        return {
            "company_id": company_id,
            "total_experiences": total,
            "sentiment_distribution": sentiment_distribution,
            "dominant_sentiment": dominant_sentiment,
            "keywords": [{"name": kw, "count": count} for kw, count in top_keywords],
            "trend_data": trend_data,
            "summary": summary,
            "confidence": confidence,
            "updated_at": experiences_response.data[-1]["created_at"] if experiences_response.data else None
        }
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des insights entreprise {company_id}: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de l'analyse des insights")

@router.get("/{company_id}/themes")
def get_company_themes(company_id: str):
    """
    Récupère les thèmes positifs et négatifs pour une entreprise
    Utilisé dans la page Insights du dashboard
    """
    try:
        # Récupérer les insights de l'entreprise
        insights_response = supabase.table("insights")\
            .select("sentiment, keywords")\
            .in_("experience_id", 
                supabase.table("experiences").select("id").eq("company_id", company_id).execute().data
            )\
            .execute()
        
        insights = insights_response.data or []
        
        # Séparer les mots-clés par sentiment
        positive_keywords = {}
        negative_keywords = {}
        
        for insight in insights:
            sentiment = insight["sentiment"]
            keywords = insight.get("keywords", [])
            
            if sentiment == "positif":
                for kw in keywords:
                    positive_keywords[kw] = positive_keywords.get(kw, 0) + 1
            elif sentiment == "negatif":
                for kw in keywords:
                    negative_keywords[kw] = negative_keywords.get(kw, 0) + 1
        
        # Formatter les thèmes
        positive_themes = [
            {"name": kw, "count": count, "trend": "up"} 
            for kw, count in sorted(positive_keywords.items(), key=lambda x: x[1], reverse=True)[:10]
        ]
        
        negative_themes = [
            {"name": kw, "count": count, "trend": "down"} 
            for kw, count in sorted(negative_keywords.items(), key=lambda x: x[1], reverse=True)[:5]
        ]
        
        return {
            "company_id": company_id,
            "positive_themes": positive_themes,
            "negative_themes": negative_themes,
            "total_themes": len(positive_themes) + len(negative_themes)
        }
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des thèmes entreprise {company_id}: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de l'analyse des thèmes")

def generate_trend_data(insights: List[Dict]) -> List[Dict]:
    """Génère les données de tendances temporelles"""
    # Pour l'instant, retourne des données mock
    # TODO: Implémenter l'analyse temporelle réelle
    return [
        {"date": "Mar 1", "positive": 45, "neutral": 30, "negative": 12},
        {"date": "Mar 8", "positive": 52, "neutral": 28, "negative": 10},
        {"date": "Mar 15", "positive": 58, "neutral": 25, "negative": 8},
        {"date": "Mar 22", "positive": 62, "neutral": 22, "negative": 7},
        {"date": "Mar 29", "positive": 67, "neutral": 20, "negative": 6},
        {"date": "Apr 5", "positive": 72, "neutral": 18, "negative": 5},
    ]

def generate_company_summary(sentiment_dist: Dict, keywords: List, total: int) -> str:
    """Génère un résumé textuel pour l'entreprise"""
    if total == 0:
        return "Aucune expérience disponible pour cette entreprise"
    
    dominant = max(sentiment_dist, key=sentiment_dist.get)
    dominant_pct = sentiment_dist[dominant]
    
    if dominant == "positif":
        sentiment_desc = f"fortement positive ({dominant_pct}%)"
    elif dominant == "negatif":
        sentiment_desc = f"préoccupante ({dominant_pct}% d'expériences négatives)"
    else:
        sentiment_desc = "neutre"
    
    top_keywords = [kw["name"] for kw in keywords[:3]] if keywords else []
    keywords_text = ", ".join(top_keywords) if top_keywords else "aucun thème particulier"
    
    return f"Votre entreprise est perçue comme {sentiment_desc}. Les thèmes les plus mentionnés sont : {keywords_text}."

def calculate_confidence(total: int, sentiment_dist: Dict) -> str:
    """Calcule le niveau de confiance de l'analyse"""
    if total < 5:
        return "Faible (peu de données)"
    elif total < 20:
        return "Moyenne"
    elif total < 50:
        return "Élevée"
    else:
        return "Très élevée"
