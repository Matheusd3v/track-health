from sqlalchemy import Column, ForeignKey, String
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class UserDrugs(db.Model):
    __tablename__ = "user_drug"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: str = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False, unique=True)
    frequency: str = Column(String, nullable=False)
    description: str = Column(String)



