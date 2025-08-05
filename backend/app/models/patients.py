from sqlalchemy import Column, Integer, String, Date, Text, Integer, ForeignKey
from backend.app.core.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    cccd = Column(String(20), unique=True, nullable=True)
