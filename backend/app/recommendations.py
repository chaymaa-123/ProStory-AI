"""
Module d'analyse de texte pour ProStory-AI
Fournit l'analyse de sentiment et l'extraction de mots-clés
"""

import re
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Analyse un texte pour en extraire le sentiment et les mots-clés
    
    Args:
        text (str): Le texte à analyser
        
    Returns:
        Dict[str, Any]: {
            "sentiment": "positif" | "neutre" | "negatif",
            "keywords": List[str],
            "confidence": float
        }
    """
    try:
        # Nettoyage du texte
        cleaned_text = clean_text(text)
        
        # Analyse de sentiment simple
        sentiment_result = analyze_sentiment_simple(cleaned_text)
        
        # Extraction de mots-clés
        keywords = extract_keywords_simple(cleaned_text)
        
        return {
            "sentiment": sentiment_result["sentiment"],
            "keywords": keywords,
            "confidence": sentiment_result["confidence"]
        }
        
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse du texte: {e}")
        return {
            "sentiment": "neutre",
            "keywords": [],
            "confidence": 0.0
        }

def clean_text(text: str) -> str:
    """
    Nettoie le texte pour l'analyse
    
    Args:
        text (str): Texte à nettoyer
        
    Returns:
        str: Texte nettoyé
    """
    # Suppression des caractères spéciaux et mise en minuscule
    text = re.sub(r'[^\w\s]', ' ', text.lower())
    # Suppression des espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def analyze_sentiment_simple(text: str) -> Dict[str, Any]:
    """
    Analyse de sentiment simple basée sur des mots-clés
    
    Args:
        text (str): Texte à analyser
        
    Returns:
        Dict[str, Any]: {"sentiment": str, "confidence": float}
    """
    # Mots-clés positifs
    positive_words = [
        'excellent', 'fantastique', 'super', 'génial', 'formidable', 'admirable',
        'bon', 'bien', 'content', 'satisfait', 'heureux', 'plaisir', 'aimer',
        'love', 'great', 'good', 'amazing', 'fantastic', 'wonderful', 'awesome',
        'positive', 'belle', 'beau', 'agréable', 'cool', 'top', 'parfait',
        'succès', 'réussite', 'opportunité', 'croissance', 'développement',
        'support', 'soutien', 'équipe', 'team', 'collaboration', 'entraide'
    ]
    
    # Mots-clés négatifs
    negative_words = [
        'mauvais', 'terrible', 'horrible', 'affreux', 'épouvantable', 'désastreux',
        'mal', 'grave', 'sérieux', 'problème', 'difficulté', 'échec', 'échouer',
        'bad', 'terrible', 'awful', 'horrible', 'disaster', 'failure',
        'stress', 'pression', 'fatigue', 'épuisement', 'burnout', 'toxique',
        'toxic', 'négatif', 'negative', 'triste', 'sad', 'angry', 'colère',
        'frustré', 'frustration', 'déçu', 'déception', 'injustice', 'harcellement'
    ]
    
    words = text.split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    total_words = len(words)
    
    if total_words == 0:
        return {"sentiment": "neutre", "confidence": 0.0}
    
    # Calcul du score
    if positive_count > negative_count:
        sentiment = "positif"
        confidence = min(positive_count / total_words * 2, 1.0)
    elif negative_count > positive_count:
        sentiment = "negatif" 
        confidence = min(negative_count / total_words * 2, 1.0)
    else:
        sentiment = "neutre"
        confidence = 0.5
    
    return {
        "sentiment": sentiment,
        "confidence": round(confidence, 2)
    }

def extract_keywords_simple(text: str) -> List[str]:
    """
    Extrait les mots-clés simples du texte
    
    Args:
        text (str): Texte à analyser
        
    Returns:
        List[str]: Liste des mots-clés
    """
    # Mots à ignorer (stop words)
    stop_words = {
        'le', 'la', 'les', 'de', 'du', 'des', 'à', 'au', 'aux', 'pour', 'avec',
        'par', 'sur', 'dans', 'en', 'vers', 'contre', 'sans', 'sous', 'selon',
        'entre', 'chez', 'pendant', 'depuis', 'jusque', 'même', 'si', 'alors',
        'que', 'qui', 'quoi', 'où', 'quand', 'comment', 'pourquoi', 'combien',
        'ce', 'cette', 'ces', 'cet', 'celui', 'celle', 'ceux', 'celles',
        'on', 'nous', 'vous', 'ils', 'elles', 'il', 'elle', 'je', 'tu',
        'me', 'te', 'se', 'lui', 'leur', 'eux', 'lui', 'y', 'en',
        'un', 'une', 'uns', 'unes', 'mon', 'ton', 'son', 'ma', 'ta', 'sa',
        'mes', 'tes', 'ses', 'notre', 'votre', 'nos', 'vos', 'leurs',
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
        'before', 'after', 'above', 'below', 'between', 'among', 'is', 'are',
        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do',
        'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
        'must', 'can', 'shall', 'this', 'that', 'these', 'those', 'i', 'you',
        'he', 'she', 'it', 'we', 'they', 'them', 'him', 'her', 'us', 'my',
        'your', 'his', 'its', 'our', 'their', 'what', 'which', 'who', 'whom',
        'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both', 'few',
        'more', 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so',
        'than', 'too', 'very', 'just', 'now', 'also', 'here', 'there', 'well'
    }
    
    # Extraction des mots (longueur minimale de 3 caractères)
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    
    # Filtrage des stop words et comptage
    word_freq = {}
    for word in words:
        if word not in stop_words and len(word) >= 3:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Tri par fréquence et prise des top 10
    keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return [keyword for keyword, freq in keywords]

# Test simple
if __name__ == "__main__":
    test_text = "J'ai adoré travailler dans cette entreprise. L'équipe est fantastique et le management est très supportant. Cependant, la charge de travail peut parfois être élevée."
    result = analyze_text(test_text)
    print(f"Résultat de l'analyse: {result}")
