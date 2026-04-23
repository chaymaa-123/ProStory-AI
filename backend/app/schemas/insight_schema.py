from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class InsightCreate(BaseModel):
    experience_id: str = Field(..., description="ID de l'expérience")
    sentiment: str = Field(..., regex="^(positif|neutre|negatif)$")
    keywords: List[str] = Field(default_factory=list)
    score: float = Field(default=0.0, ge=0.0, le=1.0)

class InsightResponse(BaseModel):
    id: UUID
    experience_id: UUID
    sentiment: str
    keywords: List[str]
    score: float
    created_at: datetime

class InsightUpdate(BaseModel):
    sentiment: Optional[str] = Field(None, regex="^(positif|neutre|negatif)$")
    keywords: Optional[List[str]] = None
    score: Optional[float] = Field(None, ge=0.0, le=1.0)

class ExperienceInsightResponse(BaseModel):
    """Response pour l'API GET /experience/{id}/insights"""
    experience_id: UUID
    sentiment: str
    keywords: List[str]
    score: float
    confidence: float
    created_at: datetime
    
    # Champs calculés
    sentiment_label: str
    sentiment_color: str
