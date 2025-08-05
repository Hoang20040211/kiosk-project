from pydantic import BaseModel
from typing import Optional
from datetime import date

class PatientCreate(BaseModel):
    full_name: str
    gender: str
    phone_number: str
    date_of_birth: date
    email: str
    address: str
    users_id: int
    cccd: Optional[str]

class PatientUpdate(BaseModel):
    full_name: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    email: Optional[str] = None
    address: Optional[str] = None
    cccd: Optional[str]

class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True 
