from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class ExperienceCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    content: str = Field(..., min_length=10)
    category: Optional[str] = None
    tags: List[str] = []
    company_id: Optional[str] = None
    event_id: Optional[str] = None

class ExperienceUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=255)
    content: Optional[str] = Field(None, min_length=10)
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    company_id: Optional[str] = None
    event_id: Optional[str] = None

class ExperienceResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    content: str
    category: Optional[str] = None
    tags: List[str] = []
    company_id: Optional[str] = None
    company_name: Optional[str] = None  # Ajouté pour le mapping auto
    event_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None


class ExperienceListResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    content: str
    tags: List[str] = []
    company_name: Optional[str] = None  # Ajouté pour le flux
    created_at: datetime

    @property
    def preview(self) -> str:
        return self.content[:200] if len(self.content) > 200 else self.content

