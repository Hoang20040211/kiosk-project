from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.crud import patients as patient_crud
import backend.app.schemas.patients as patient_schema
from backend.app.models.patients import Patient

router = APIRouter(prefix="/patients", tags=["Patients"])
@router.get("/patients/by-cccd/{cccd}")
def get_patient_by_cccd(cccd: str, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.cccd == cccd).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
@router.post("/", response_model=patient_schema.PatientResponse)
def create_patient(patient: patient_schema.PatientCreate, db: Session = Depends(get_db)):
    return patient_crud.create_patient(db, patient)

@router.get("/{patient_id}", response_model=patient_schema.PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = patient_crud.get_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.get("/", response_model=list[patient_schema.PatientResponse])
def list_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return patient_crud.get_all_patients(db, skip, limit)

@router.put("/{patient_id}", response_model=patient_schema.PatientResponse)
def update_patient(patient_id: int, patient: patient_schema.PatientUpdate, db: Session = Depends(get_db)):
    db_patient = patient_crud.update_patient(db, patient_id, patient)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.delete("/{patient_id}", response_model=patient_schema.PatientResponse)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = patient_crud.delete_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient
