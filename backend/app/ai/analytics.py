"""
Endpoint FastAPI pour l'analyse IA de ProStory-AI
Expose les fonctionnalités d'analyse via API REST
"""

from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
import logging

from .pipeline import process_experiences, test_pipeline

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Création du routeur
router = APIRouter(prefix="/ai", tags=["AI Analytics"])

# Modèles Pydantic pour la validation
class ExperienceInput(BaseModel):
    content: str
    author_id: Optional[str] = None
    company_id: Optional[str] = None
    timestamp: Optional[str] = None

class CompanyInsightsRequest(BaseModel):
    company_id: str
    max_experiences: Optional[int] = 30
    include_summary: Optional[bool] = True

class BatchAnalysisRequest(BaseModel):
    experiences: List[ExperienceInput]
    max_experiences: Optional[int] = 30

# Endpoints principaux
@router.get("/company/{company_id}/insights")
async def get_company_insights(
    company_id: str,
    max_experiences: int = Query(30, le=100, description="Nombre max d'expériences à analyser"),
    include_summary: bool = Query(True, description="Inclure un résumé textuel")
):
    """
    Analyse les insights pour une entreprise spécifique
    
    Args:
        company_id (str): ID de l'entreprise
        max_experiences (int): Nombre max d'expériences à traiter
        include_summary (bool): Inclure le résumé textuel
        
    Returns:
        Dict[str, Any]: Insights complets de l'entreprise
    """
    try:
        logger.info(f"Demande d'insights pour l'entreprise {company_id}")
        
        # TODO: Récupérer depuis la base de données Supabase
        # Pour l'instant, données de test
        experiences = get_test_experiences(company_id)
        
        if not experiences:
            logger.warning(f"Aucune expérience trouvée pour l'entreprise {company_id}")
            return create_empty_insights(company_id)
        
        # Traitement via le pipeline IA
        result = process_experiences(experiences, max_experiences)
        
        # Ajouter les métadonnées de l'entreprise
        result["company_id"] = company_id
        result["request_params"] = {
            "max_experiences": max_experiences,
            "include_summary": include_summary
        }
        
        logger.info(f"Insights générés pour {company_id}: {result['total']} expériences analysées")
        
        return result
        
    except Exception as e:
        logger.error(f"Erreur lors de la génération des insights pour {company_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse: {str(e)}")

@router.post("/batch/analyze")
async def batch_analyze_experiences(request: BatchAnalysisRequest):
    """
    Analyse un lot d'expériences
    
    Args:
        request (BatchAnalysisRequest): Données du lot à analyser
        
    Returns:
        Dict[str, Any]: Résultats de l'analyse batch
    """
    try:
        logger.info(f"Analyse batch de {len(request.experiences)} expériences")
        
        # Convertir les expériences en format attendu par le pipeline
        experiences = [
            {"content": exp.content, "author_id": exp.author_id, "company_id": exp.company_id}
            for exp in request.experiences
        ]
        
        # Traitement via le pipeline
        result = process_experiences(experiences, request.max_experiences)
        
        # Ajouter les métadonnées du batch
        result["batch_metadata"] = {
            "total_requested": len(request.experiences),
            "processed": result["processed_experiences"],
            "max_limit": request.max_experiences
        }
        
        logger.info(f"Batch analysé: {result['processed_experiences']}/{len(request.experiences)} expériences")
        
        return result
        
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse batch: {e}")
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse: {str(e)}")

@router.get("/test")
async def test_ai_pipeline():
    """
    Endpoint de test pour le pipeline IA
    
    Returns:
        Dict[str, Any]: Résultats du test avec données fictives
    """
    try:
        logger.info("Test du pipeline IA demandé")
        
        result = test_pipeline()
        
        return {
            "status": "success",
            "message": "Pipeline IA testé avec succès",
            "test_results": result
        }
        
    except Exception as e:
        logger.error(f"Erreur lors du test du pipeline: {e}")
        raise HTTPException(status_code=500, detail=f"Erreur lors du test: {str(e)}")

@router.get("/health")
async def health_check():
    """
    Vérification de la santé du service IA
    
    Returns:
        Dict[str, str]: Status du service
    """
    return {
        "status": "healthy",
        "service": "ProStory-AI Analytics",
        "version": "1.0.0"
    }

# Fonctions utilitaires
def get_test_experiences(company_id: str) -> List[Dict[str, str]]:
    """
    Génère des expériences de test pour le développement
    
    Args:
        company_id (str): ID de l'entreprise
        
    Returns:
        List[Dict[str, str]]: Expériences de test
    """
    # Données de test variées avec différents sentiments
    test_data = [
        {"content": "Great management and amazing team spirit, really enjoy working here"},
        {"content": "Poor communication from leadership and bad organization in projects"},
        {"content": "Excellent work events and team building activities, but some management issues"},
        {"content": "Good work-life balance and very supportive colleagues"},
        {"content": "Toxic environment with high pressure and unrealistic deadlines"},
        {"content": "Innovative projects and opportunities for growth, fantastic learning environment"},
        {"content": "Low salary compared to market standards, but good benefits package"},
        {"content": "Strong company culture and values alignment with personal principles"},
        {"content": "Lack of career advancement opportunities and recognition"},
        {"content": "Flexible working hours and remote work options are great benefits"},
        {"content": "Management needs improvement in communication and feedback processes"},
        {"content": "Amazing products and services that make me proud to work here"},
        {"content": "Workload can be overwhelming during peak seasons, need better resource planning"},
        {"content": "Great training programs and professional development opportunities"},
        {"content": "Office environment needs improvement, better facilities and equipment needed"}
    ]
    
    # Ajouter l'ID de l'entreprise à chaque expérience
    for exp in test_data:
        exp["company_id"] = company_id
    
    return test_data

def create_empty_insights(company_id: str) -> Dict[str, Any]:
    """
    Crée des insights vides pour une entreprise sans données
    
    Args:
        company_id (str): ID de l'entreprise
        
    Returns:
        Dict[str, Any]: Insights vides
    """
    return {
        "company_id": company_id,
        "positive": 0.0,
        "negative": 0.0,
        "neutral": 0.0,
        "total": 0,
        "dominant_sentiment": "neutral",
        "keywords": [],
        "keyword_count": 0,
        "summary": f"Aucune expérience disponible pour l'entreprise {company_id}",
        "confidence": "Very Low (no data)",
        "trends": ["Aucune donnée disponible"],
        "recommendations": ["Commencer par collecter des expériences des employés"],
        "processed_experiences": 0,
        "max_experiences_limit": 30,
        "analysis_timestamp": "",
        "error": None
    }

# Middleware pour le logging des requêtes
# @router.middleware("http")
async def log_requests(request, call_next):
    """Log toutes les requêtes pour monitoring"""
    logger.info(f"Requête IA: {request.method} {request.url}")
    response = await call_next(request)
    return response
