from sqlalchemy.orm import Session
from backend.app.models.patients import Patient
from backend.app.schemas.patients import PatientCreate, PatientUpdate

def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_all_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Patient).offset(skip).limit(limit).all()

def update_patient(db: Session, patient_id: int, patient_update: PatientUpdate):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        return None
    for field, value in patient_update.dict(exclude_unset=True).items():
        setattr(db_patient, field, value)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        return None
    db.delete(db_patient)
    db.commit()
    return db_patient
