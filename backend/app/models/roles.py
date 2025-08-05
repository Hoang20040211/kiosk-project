from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.core.database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)