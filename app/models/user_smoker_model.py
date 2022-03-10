from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Date, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


@dataclass
class UserSmoker(db.Model):

    __tablename__ = "user_smoker"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete="CASCADE"), nullable = False, unique = True)
    frequency:str = Column(String, nullable = False)
    description:str = Column(String)
