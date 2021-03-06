from sqlalchemy import Column, String, Integer
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class AddressModel(db.Model):
    
    __tablename__ = "address"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    street: str = Column(String(250), nullable=False)
    number: int = Column(Integer, nullable=False)
    district: str = Column(String(50))
    city: str = Column(String(50))
    complement: str = Column(String(250))

