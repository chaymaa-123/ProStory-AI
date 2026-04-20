"""
Module IA pour ProStory-AI
Fournit des fonctionnalités d'analyse de sentiment, extraction de mots-clés et génération d'insights
"""

from .sentiment import analyze_sentiment, batch_analyze_sentiment
from .keywords import extract_keywords, extract_keywords_with_scores, batch_extract_keywords
from .summary import generate_summary, generate_insights_summary
from .pipeline import process_experiences, test_pipeline
from .analytics import router

__version__ = "1.0.0"
__author__ = "ProStory-AI Team"

# Export des fonctions principales
__all__ = [
    # Analyse de sentiment
    "analyze_sentiment",
    "batch_analyze_sentiment",
    
    # Extraction de mots-clés
    "extract_keywords", 
    "extract_keywords_with_scores",
    "batch_extract_keywords",
    
    # Génération de résumés
    "generate_summary",
    "generate_insights_summary",
    
    # Pipeline principal
    "process_experiences",
    "test_pipeline",
    
    # Router FastAPI
    "router"
]

# Configuration du module
def get_module_info():
    """
    Retourne les informations du module IA
    
    Returns:
        dict: Informations du module
    """
    return {
        "name": "ProStory-AI Analytics Module",
        "version": __version__,
        "description": "Module d'analyse IA pour les expériences professionnelles",
        "features": [
            "Analyse de sentiment avec Transformers",
            "Extraction de mots-clés avec KeyBERT", 
            "Génération de résumés intelligents",
            "Pipeline d'analyse complet",
            "API REST FastAPI"
        ],
        "dependencies": [
            "transformers",
            "keybert", 
            "torch",
            "numpy",
            "fastapi"
        ]
    }

if __name__ == "__main__":
    # Test du module
    print("🤖 Module IA ProStory-AI")
    print(get_module_info())
    print("\n🧪 Test du pipeline...")
    result = test_pipeline()
    print("✅ Test terminé avec succès!")
