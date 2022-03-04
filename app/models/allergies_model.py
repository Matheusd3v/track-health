from sqlalchemy import Column, String
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class AllergyModel(db.Model):

    __tablename__ = "allergies"


    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: str = Column(String(100), nullable=False)
    
