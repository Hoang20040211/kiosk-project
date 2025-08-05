from sqlalchemy import Column, Integer, String, Text
from backend.app.core.database import Base

class Specialty(Base):
    __tablename__ = "specialties"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
