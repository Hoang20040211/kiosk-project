from fastapi import FastAPI
from backend.app.core.database import engine, Base
from backend.app.routers import patients, appointments, services, auth
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(patients.router)
# app.include_router(appointments.router)
# app.include_router(services.router)
# app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hoặc cụ thể như ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)