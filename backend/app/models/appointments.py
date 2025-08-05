from sqlalchemy import Column, Integer, Integer, DateTime, String, Text, ForeignKey
from backend.app.core.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String(255), nullable=False)
    note = Column(Text, nullable=False)
