from sqlalchemy import Column, ForeignKey, String
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class UserAllergyModel(db.Model):

    __tablename__ = "user_allergies"


    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description: str = Column(String(200), nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)
    allergy_id = Column(UUID(as_uuid=True), ForeignKey('allergies.id'), nullable = False)