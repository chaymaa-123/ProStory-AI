"""
Module d'analyse de sentiment pour ProStory-AI
Utilise Transformers de Hugging Face pour l'analyse de sentiment
"""

from transformers import pipeline
from typing import Dict, Any
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialisation du pipeline de sentiment (chargé au démarrage)
try:
    sentiment_pipeline = pipeline("sentiment-analysis")
    logger.info("Pipeline de sentiment initialisé avec succès")
except Exception as e:
    logger.error(f"Erreur lors de l'initialisation du pipeline de sentiment: {e}")
    sentiment_pipeline = None

def analyze_sentiment(text: str) -> Dict[str, Any]:
    """
    Analyse le sentiment d'un texte donné
    
    Args:
        text (str): Le texte à analyser
        
    Returns:
        Dict[str, Any]: Dictionnaire contenant le sentiment et la confiance
    """
    if not sentiment_pipeline:
        logger.error("Pipeline de sentiment non disponible")
        return {
            "sentiment": "neutral",
            "confidence": 0.0,
            "error": "Pipeline non initialisé"
        }
    
    if not text or not text.strip():
        return {
            "sentiment": "neutral",
            "confidence": 0.0,
            "error": "Texte vide"
        }
    
    try:
        # Limiter la longueur du texte pour éviter les timeouts
        text = text[:512]  # Limite raisonnable pour les modèles
        
        result = sentiment_pipeline(text)[0]
        
        label = result["label"].lower()  # POSITIVE / NEGATIVE
        score = result["score"]
        
        # Normalisation des labels
        if label in ["positive", "pos", "label_1"]:
            sentiment = "positive"
        elif label in ["negative", "neg", "label_0"]:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        return {
            "sentiment": sentiment,
            "confidence": round(score, 2)
        }
        
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse de sentiment: {e}")
        return {
            "sentiment": "neutral",
            "confidence": 0.0,
            "error": str(e)
        }

def batch_analyze_sentiment(texts: list) -> list:
    """
    Analyse le sentiment de plusieurs textes (batch processing)
    
    Args:
        texts (list): Liste des textes à analyser
        
    Returns:
        list: Liste des résultats d'analyse
    """
    results = []
    for text in texts:
        result = analyze_sentiment(text)
        results.append(result)
    
    return results
