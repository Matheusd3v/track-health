from sqlalchemy import Column, ForeignKey, String
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.allergies_model import AllergyModel
from app.models.user_model import User


@dataclass
class UserAllergyModel(db.Model):

    __tablename__ = "user_allergies"


    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description: str = Column(String(200))

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)
    allergy_id = Column(UUID(as_uuid=True), ForeignKey('allergies.id'), nullable = False, unique=True)

    allergy: AllergyModel = relationship("AllergyModel", uselist=False, 
        backref="allergy_name")

