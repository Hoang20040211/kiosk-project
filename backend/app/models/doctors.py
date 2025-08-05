from sqlalchemy import Column, Integer, String, Integer, ForeignKey
from backend.app.core.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    specialty_id = Column(Integer, ForeignKey("specialties.id"), nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
