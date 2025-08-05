from sqlalchemy import Column, Integer, String, Text, Numeric, Integer, ForeignKey
from backend.app.core.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
