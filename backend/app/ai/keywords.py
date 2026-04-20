"""
Module d'extraction de mots-clés pour ProStory-AI
Utilise KeyBERT pour extraire les mots-clés pertinents
"""

from keybert import KeyBERT
from typing import List, Dict, Any
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialisation du modèle KeyBERT (chargé au démarrage)
try:
    kw_model = KeyBERT()
    logger.info("Modèle KeyBERT initialisé avec succès")
except Exception as e:
    logger.error(f"Erreur lors de l'initialisation de KeyBERT: {e}")
    kw_model = None

def extract_keywords(text: str, top_n: int = 5, language: str = "english") -> List[str]:
    """
    Extrait les mots-clés d'un texte donné
    
    Args:
        text (str): Le texte à analyser
        top_n (int): Nombre de mots-clés à extraire (défaut: 5)
        language (str): Langue des stop words (défaut: "english")
        
    Returns:
        List[str]: Liste des mots-clés extraits
    """
    if not kw_model:
        logger.error("Modèle KeyBERT non disponible")
        return []
    
    if not text or not text.strip():
        return []
    
    try:
        # Limiter la longueur du texte pour éviter les timeouts
        text = text[:512]  # Limite raisonnable pour KeyBERT
        
        # Extraction des mots-clés
        keywords = kw_model.extract_keywords(
            text,
            top_n=top_n,
            stop_words=language,
            keyphrase_ngram_range=(1, 2),  # Mots simples et paires
            use_maxsum=True,  # Diversité maximale
            use_mmr=True,  # Maximal Marginal Relevance
            diversity=0.7  # Diversité des résultats
        )
        
        # Retourner seulement les mots-clés (sans les scores)
        return [kw[0] for kw in keywords]
        
    except Exception as e:
        logger.error(f"Erreur lors de l'extraction des mots-clés: {e}")
        return []

def extract_keywords_with_scores(text: str, top_n: int = 5, language: str = "english") -> List[Dict[str, Any]]:
    """
    Extrait les mots-clés avec leurs scores de pertinence
    
    Args:
        text (str): Le texte à analyser
        top_n (int): Nombre de mots-clés à extraire
        language (str): Langue des stop words
        
    Returns:
        List[Dict[str, Any]]: Liste des mots-clés avec scores
    """
    if not kw_model:
        logger.error("Modèle KeyBERT non disponible")
        return []
    
    if not text or not text.strip():
        return []
    
    try:
        text = text[:512]
        
        keywords = kw_model.extract_keywords(
            text,
            top_n=top_n,
            stop_words=language,
            keyphrase_ngram_range=(1, 2),
            use_maxsum=True,
            use_mmr=True,
            diversity=0.7
        )
        
        # Formater les résultats avec scores
        return [
            {
                "keyword": kw[0],
                "score": round(kw[1], 3)
            }
            for kw in keywords
        ]
        
    except Exception as e:
        logger.error(f"Erreur lors de l'extraction des mots-clés avec scores: {e}")
        return []

def batch_extract_keywords(texts: list, max_texts: int = 20) -> List[str]:
    """
    Extrait les mots-clés de plusieurs textes (limité pour la performance)
    
    Args:
        texts (list): Liste des textes à analyser
        max_texts (int): Nombre maximum de textes à traiter
        
    Returns:
        List[str]: Liste combinée des mots-clés
    """
    if not texts:
        return []
    
    # Limiter le nombre de textes pour éviter les timeouts
    texts = texts[:max_texts]
    
    all_keywords = []
    
    for text in texts:
        keywords = extract_keywords(text)
        all_keywords.extend(keywords)
    
    return all_keywords

def get_top_keywords_by_frequency(keywords: List[str], top_n: int = 10) -> List[tuple]:
    """
    Retourne les mots-clés les plus fréquents
    
    Args:
        keywords (List[str]): Liste des mots-clés
        top_n (int): Nombre de mots-clés à retourner
        
    Returns:
        List[tuple]: Liste des (mot-clé, fréquence)
    """
    from collections import Counter
    
    if not keywords:
        return []
    
    # Compter les fréquences
    keyword_counts = Counter(keywords)
    
    # Retourner les plus fréquents
    return keyword_counts.most_common(top_n)
