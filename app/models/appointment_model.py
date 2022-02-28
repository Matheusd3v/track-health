from sqlalchemy import Column, ForeignKey, String, Date
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class AppointmentModel(db.Model):
    __tablename__ = "appointments"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: str = Column(String(100), nullable=False)
    date: str = Column(Date, nullable=False)
    description: str = Column(String(200))

    user_id: str = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)

    doctor_id: str = Column(UUID(as_uuid=True), ForeignKey('doctors.id'), nullable=False)
