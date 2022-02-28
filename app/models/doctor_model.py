from enum import unique
from sqlalchemy import Column, ForeignKey, String, Integer
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class DoctorModel(db.Model):

    __tablename__ = "doctors"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: str = Column(String(100), nullable=False)
    type: str = Column(String(50), nullable=False)
    email: str = Column(String(50))
    phone: str = Column(String(50), unique=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)

    # adress_id: str = Column(UUID(as_uuid=True), ForeignKey('adress.id'), nullable=False)
