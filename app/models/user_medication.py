from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, ForeignKey,String
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.medication_model import Medication

@dataclass
class UserMedication(db.Model):

    __tablename__ = "user_medication"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id:str = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    medication_id:str = Column(UUID(as_uuid=True), ForeignKey("medications.id"))
    description:str = Column(String)

    medication:Medication = relationship("Medication",backref="medication_user") 