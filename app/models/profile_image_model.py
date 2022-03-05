from sqlalchemy import Column, ForeignKey, String
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class ProfileImageModel(db.Model):
    __tablename__ = "profile_image"

    id: str = Column(String, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False, unique=True)
    name: str = Column(String, nullable=False)
    url: str = Column(String, nullable=False)
