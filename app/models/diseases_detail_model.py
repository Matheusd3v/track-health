from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Date, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class DiseasesDetailModel(db.Model):

    __tablename__ = "diseases_detail"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description: str = Column(String)
    medication: str = Column(String)
