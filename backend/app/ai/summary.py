"""
Module de génération de résumés pour ProStory-AI
Crée des résumés intelligents basés sur les analyses de sentiment et mots-clés
"""

from typing import Dict, Any, List
import logging
from datetime import datetime

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_summary(data: Dict[str, Any]) -> str:
    """
    Génère un résumé textuel basé sur les données d'analyse
    
    Args:
        data (Dict[str, Any]): Données d'analyse (sentiments, mots-clés, etc.)
        
    Returns:
        str: Résumé formaté
    """
    try:
        # Extraire les informations principales
        total = data.get('total', 0)
        dominant_sentiment = data.get('dominant_sentiment', 'neutral')
        keywords = data.get('keywords', [])
        
        # Séparer les mots-clés par sentiment si disponible
        positive_keywords = []
        negative_keywords = []
        neutral_keywords = []
        
        # Si les données détaillées sont disponibles
        if 'detailed_keywords' in data:
            for kw_info in data['detailed_keywords']:
                keyword = kw_info.get('keyword', '')
                sentiment = kw_info.get('sentiment', 'neutral')
                
                if sentiment == 'positive':
                    positive_keywords.append(keyword)
                elif sentiment == 'negative':
                    negative_keywords.append(keyword)
                else:
                    neutral_keywords.append(keyword)
        else:
            # Utiliser les mots-clés généraux
            all_keywords = [kw[0] if isinstance(kw, tuple) else kw for kw in keywords]
            neutral_keywords = all_keywords[:5]
        
        # Générer le résumé
        summary = f"""
📊 **Analyse de l'entreprise**

Cette période, l'entreprise est principalement perçue comme **{dominant_sentiment}**.

📈 **Statistiques clés :**
- Total d'expériences analysées : {total}
- Sentiment dominant : {dominant_sentiment}

💪 **Points forts :**
{format_keywords_list(positive_keywords[:3]) if positive_keywords else "- Aucun point fort identifié"}

⚠️ **Axes d'amélioration :**
{format_keywords_list(negative_keywords[:3]) if negative_keywords else "- Aucune faiblesse majeure identifiée"}

🔑 **Mots-clés principaux :**
{format_keywords_list([kw[0] if isinstance(kw, tuple) else kw for kw in keywords[:5]])}

📅 **Analyse générée le :** {datetime.now().strftime('%d/%m/%Y à %H:%M')}
"""
        
        return summary.strip()
        
    except Exception as e:
        logger.error(f"Erreur lors de la génération du résumé: {e}")
        return "Erreur lors de la génération du résumé"

def format_keywords_list(keywords: List[str]) -> str:
    """
    Formate une liste de mots-clés pour l'affichage
    
    Args:
        keywords (List[str]): Liste des mots-clés
        
    Returns:
        str: Liste formatée
    """
    if not keywords:
        return "- Aucun mot-clé"
    
    return "\n".join([f"- {kw}" for kw in keywords])

def generate_insights_summary(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Génère un résumé structuré avec des insights supplémentaires
    
    Args:
        data (Dict[str, Any]): Données d'analyse
        
    Returns:
        Dict[str, Any]: Résumé structuré
    """
    try:
        total = data.get('total', 0)
        
        # Calculer le niveau de confiance
        confidence_level = calculate_confidence_level(total)
        
        # Identifier les tendances
        trends = identify_trends(data)
        
        # Générer des recommandations
        recommendations = generate_recommendations(data)
        
        return {
            "summary": generate_summary(data),
            "confidence": confidence_level,
            "trends": trends,
            "recommendations": recommendations,
            "data_points": total
        }
        
    except Exception as e:
        logger.error(f"Erreur lors de la génération du résumé structuré: {e}")
        return {
            "summary": "Erreur lors de l'analyse",
            "confidence": "Low",
            "trends": [],
            "recommendations": [],
            "data_points": 0
        }

def calculate_confidence_level(total_experiences: int) -> str:
    """
    Calcule le niveau de confiance basé sur le nombre d'expériences
    
    Args:
        total_experiences (int): Nombre total d'expériences
        
    Returns:
        str: Niveau de confiance
    """
    if total_experiences >= 100:
        return "Very High (based on 100+ experiences)"
    elif total_experiences >= 50:
        return "High (based on 50+ experiences)"
    elif total_experiences >= 20:
        return "Medium (based on 20+ experiences)"
    elif total_experiences >= 10:
        return "Low (based on 10+ experiences)"
    else:
        return "Very Low (based on less than 10 experiences)"

def identify_trends(data: Dict[str, Any]) -> List[str]:
    """
    Identifie les tendances basées sur les données
    
    Args:
        data (Dict[str, Any]): Données d'analyse
        
    Returns:
        List[str]: Liste des tendances identifiées
    """
    trends = []
    
    positive_pct = data.get('positive', 0)
    negative_pct = data.get('negative', 0)
    
    if positive_pct >= 70:
        trends.append("Très forte perception positive")
    elif positive_pct >= 50:
        trends.append("Perception majoritairement positive")
    
    if negative_pct >= 30:
        trends.append("Significatifs points d'amélioration identifiés")
    
    if data.get('total', 0) < 10:
        trends.append("Données limitées - plus d'expériences nécessaires")
    
    return trends

def generate_recommendations(data: Dict[str, Any]) -> List[str]:
    """
    Génère des recommandations basées sur l'analyse
    
    Args:
        data (Dict[str, Any]): Données d'analyse
        
    Returns:
        List[str]: Liste des recommandations
    """
    recommendations = []
    
    positive_pct = data.get('positive', 0)
    negative_pct = data.get('negative', 0)
    total = data.get('total', 0)
    
    if negative_pct > 40:
        recommendations.append("Investiguer les causes de la perception négative")
    
    if positive_pct > 70:
        recommendations.append("Capitaliser sur les points forts identifiés")
    
    if total < 20:
        recommendations.append("Encourager plus de collaborateurs à partager leurs expériences")
    
    # Recommandations basées sur les mots-clés
    keywords = data.get('keywords', [])
    if keywords:
        top_keyword = keywords[0][0] if isinstance(keywords[0], tuple) else keywords[0]
        recommendations.append(f"Approfondir l'analyse du thème : {top_keyword}")
    
    return recommendations
