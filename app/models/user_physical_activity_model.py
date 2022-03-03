from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Date, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.models.user_model import User
from sqlalchemy.orm import relationship


@dataclass
class UserPhysicalActivity(db.Model):

    __tablename__ = "user_physical_activity"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)
    frequency:str = Column(String, nullable = False)
    description:str = Column(String)

    User:User = relationship("User",backref="users", uselist=False)    