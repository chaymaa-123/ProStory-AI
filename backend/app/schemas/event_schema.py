from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class EventCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    date: datetime = Field(...)
    location: str = Field(..., max_length=200)
    category: str = Field(..., max_length=50)
    is_virtual: bool = Field(default=False)
    max_attendees: Optional[int] = Field(None, gt=0)
    company_id: Optional[UUID] = None  # Si créé par une entreprise

class EventUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, min_length=1, max_length=1000)
    date: Optional[datetime] = None
    location: Optional[str] = Field(None, max_length=200)
    category: Optional[str] = Field(None, max_length=50)
    is_virtual: Optional[bool] = None
    max_attendees: Optional[int] = Field(None, gt=0)

class EventResponse(BaseModel):
    id: UUID
    title: str
    description: str
    date: datetime
    location: str
    category: str
    is_virtual: bool
    max_attendees: Optional[int]
    creator_id: UUID
    company_id: Optional[UUID]
    created_at: datetime
    updated_at: datetime
    
    # Champs calculés
    attendee_count: int = 0
    experience_count: int = 0

class EventListResponse(BaseModel):
    id: UUID
    title: str
    date: datetime
    location: str
    category: str
    is_virtual: bool
    attendee_count: int = 0
    experience_count: int = 0
