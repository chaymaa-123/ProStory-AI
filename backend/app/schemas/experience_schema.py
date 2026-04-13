from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ExperienceCreate(BaseModel):
    titre: str = Field(..., min_length=3, max_length=255)
    contenu: str = Field(..., min_length=10)
    tags: Optional[str] = None
    domaine_activite: Optional[str] = None


class ExperienceUpdate(BaseModel):
    titre: Optional[str] = Field(None, min_length=3, max_length=255)
    contenu: Optional[str] = Field(None, min_length=10)
    tags: Optional[str] = None
    domaine_activite: Optional[str] = None


class ExperienceResponse(BaseModel):
    id: int
    utilisateur_id: int
    titre: str
    contenu: str
    tags: Optional[str] = None
    domaine_activite: Optional[str] = None
    sentiment: Optional[str] = None
    score_qualite: float
    date_creation: datetime
    date_modification: datetime


class ExperienceListResponse(BaseModel):
    id: int
    utilisateur_id: int
    titre: str
    contenu: str
    tags: Optional[str] = None
    sentiment: Optional[str] = None
    score_qualite: float
    date_creation: datetime

    @property
    def preview(self) -> str:
        return self.contenu[:200] if len(self.contenu) > 200 else self.contenu
