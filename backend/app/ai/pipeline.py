"""
Pipeline principal d'analyse IA pour ProStory-AI
Combine toutes les analyses : sentiment, mots-clés, et résumés
"""

from .sentiment import analyze_sentiment
from .keywords import extract_keywords, get_top_keywords_by_frequency
from .summary import generate_insights_summary
from collections import Counter
from typing import Dict, Any, List
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_experiences(experiences: List[Dict[str, Any]], max_experiences: int = 30) -> Dict[str, Any]:
    """
    Pipeline principal d'analyse des expériences
    
    Args:
        experiences (List[Dict[str, Any]]): Liste des expériences à analyser
        max_experiences (int): Nombre maximum d'expériences à traiter (performance)
        
    Returns:
        Dict[str, Any]: Résultats complets de l'analyse
    """
    try:
        # Limiter le nombre d'expériences pour la performance
        if len(experiences) > max_experiences:
            experiences = experiences[:max_experiences]
            logger.info(f"Limité à {max_experiences} expériences pour la performance")
        
        if not experiences:
            return create_empty_result()
        
        logger.info(f"Début de l'analyse de {len(experiences)} expériences")
        
        # Initialisation des variables
        sentiments = []
        all_keywords = []
        detailed_keywords = []
        
        # Traitement de chaque expérience
        for i, exp in enumerate(experiences):
            try:
                text = exp.get("content", "")
                if not text or not text.strip():
                    continue
                
                # 1. Analyse de sentiment
                sentiment_result = analyze_sentiment(text)
                sentiments.append(sentiment_result["sentiment"])
                
                # 2. Extraction de mots-clés
                keywords = extract_keywords(text, top_n=3)
                all_keywords.extend(keywords)
                
                # 3. Mots-clés détaillés avec sentiment
                for keyword in keywords:
                    detailed_keywords.append({
                        "keyword": keyword,
                        "sentiment": sentiment_result["sentiment"],
                        "confidence": sentiment_result["confidence"]
                    })
                
                # Log de progression
                if (i + 1) % 10 == 0:
                    logger.info(f"Progression : {i + 1}/{len(experiences)} expériences traitées")
                    
            except Exception as e:
                logger.error(f"Erreur lors du traitement de l'expérience {i}: {e}")
                continue
        
        # Calcul des statistiques
        stats = calculate_statistics(sentiments)
        
        # Analyse des mots-clés
        keyword_analysis = analyze_keywords(all_keywords)
        
        # Génération du résumé complet
        summary_data = {
            "total": len(sentiments),
            "dominant_sentiment": stats["dominant_sentiment"],
            "positive": stats["positive_pct"],
            "negative": stats["negative_pct"],
            "neutral": stats["neutral_pct"],
            "keywords": keyword_analysis["top_keywords"],
            "detailed_keywords": detailed_keywords
        }
        
        summary_result = generate_insights_summary(summary_data)
        
        # Construction du résultat final
        result = {
            # Statistiques principales
            "positive": stats["positive_pct"],
            "negative": stats["negative_pct"],
            "neutral": stats["neutral_pct"],
            "total": len(sentiments),
            "dominant_sentiment": stats["dominant_sentiment"],
            
            # Mots-clés
            "keywords": keyword_analysis["top_keywords"],
            "keyword_count": len(set(all_keywords)),
            
            # Résumé et insights
            "summary": summary_result["summary"],
            "confidence": summary_result["confidence"],
            "trends": summary_result["trends"],
            "recommendations": summary_result["recommendations"],
            
            # Métadonnées
            "processed_experiences": len(sentiments),
            "max_experiences_limit": max_experiences,
            "analysis_timestamp": get_timestamp()
        }
        
        logger.info(f"Analyse terminée : {len(sentiments)} expériences traitées")
        return result
        
    except Exception as e:
        logger.error(f"Erreur lors du traitement des expériences: {e}")
        return create_error_result(str(e))

def calculate_statistics(sentiments: List[str]) -> Dict[str, Any]:
    """
    Calcule les statistiques de sentiment
    
    Args:
        sentiments (List[str]): Liste des sentiments
        
    Returns:
        Dict[str, Any]: Statistiques calculées
    """
    if not sentiments:
        return {
            "positive": 0,
            "negative": 0,
            "neutral": 0,
            "positive_pct": 0.0,
            "negative_pct": 0.0,
            "neutral_pct": 0.0,
            "dominant_sentiment": "neutral"
        }
    
    total = len(sentiments)
    counts = Counter(sentiments)
    
    positive = counts.get("positive", 0)
    negative = counts.get("negative", 0)
    neutral = counts.get("neutral", 0)
    
    # Calcul des pourcentages
    positive_pct = round(positive / total * 100, 1) if total else 0
    negative_pct = round(negative / total * 100, 1) if total else 0
    neutral_pct = round(neutral / total * 100, 1) if total else 0
    
    # Sentiment dominant
    dominant_sentiment = counts.most_common(1)[0][0] if total else "neutral"
    
    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "positive_pct": positive_pct,
        "negative_pct": negative_pct,
        "neutral_pct": neutral_pct,
        "dominant_sentiment": dominant_sentiment
    }

def analyze_keywords(keywords: List[str]) -> Dict[str, Any]:
    """
    Analyse les mots-clés extraits
    
    Args:
        keywords (List[str]): Liste des mots-clés
        
    Returns:
        Dict[str, Any]: Analyse des mots-clés
    """
    if not keywords:
        return {
            "top_keywords": [],
            "unique_keywords": 0,
            "total_mentions": 0
        }
    
    # Compter les fréquences
    keyword_counts = Counter(keywords)
    
    # Top mots-clés avec fréquences
    top_keywords = keyword_counts.most_common(10)
    
    return {
        "top_keywords": top_keywords,
        "unique_keywords": len(set(keywords)),
        "total_mentions": len(keywords)
    }

def create_empty_result() -> Dict[str, Any]:
    """
    Crée un résultat vide pour le cas où aucune expérience n'est fournie
    
    Returns:
        Dict[str, Any]: Résultat vide
    """
    return {
        "positive": 0.0,
        "negative": 0.0,
        "neutral": 0.0,
        "total": 0,
        "dominant_sentiment": "neutral",
        "keywords": [],
        "keyword_count": 0,
        "summary": "Aucune expérience à analyser",
        "confidence": "Very Low (no data)",
        "trends": ["Aucune donnée disponible"],
        "recommendations": ["Commencer par collecter des expériences"],
        "processed_experiences": 0,
        "max_experiences_limit": 30,
        "analysis_timestamp": get_timestamp(),
        "error": None
    }

def create_error_result(error_message: str) -> Dict[str, Any]:
    """
    Crée un résultat d'erreur
    
    Args:
        error_message (str): Message d'erreur
        
    Returns:
        Dict[str, Any]: Résultat d'erreur
    """
    return {
        "positive": 0.0,
        "negative": 0.0,
        "neutral": 0.0,
        "total": 0,
        "dominant_sentiment": "neutral",
        "keywords": [],
        "keyword_count": 0,
        "summary": f"Erreur lors de l'analyse : {error_message}",
        "confidence": "Error",
        "trends": [],
        "recommendations [],
        "processed_experiences": 0,
        "max_experiences_limit": 30,
        "analysis_timestamp": get_timestamp(),
        "error": error_message
    }

def get_timestamp() -> str:
    """
    Génère un timestamp formaté
    
    Returns:
        str: Timestamp actuel
    """
    from datetime import datetime
    return datetime.now().isoformat()

# Fonction utilitaire pour tester le pipeline
def test_pipeline():
    """
    Fonction de test pour le pipeline avec des données fictives
    """
    test_experiences = [
        {"content": "Great management and amazing team spirit"},
        {"content": "Poor communication and bad organization"},
        {"content": "Excellent work events but some management issues"},
        {"content": "Good work-life balance and supportive colleagues"},
        {"content": "Toxic environment and high pressure"}
    ]
    
    result = process_experiences(test_experiences)
    return result

if __name__ == "__main__":
    # Test du pipeline
    print("Test du pipeline IA...")
    result = test_pipeline()
    print("Résultat du test :")
    print(result)
