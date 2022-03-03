from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class UserAlcoholic(db.Model):

    __tablename__ = "user_alcoholic"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False, unique = True)
    frequency:str = Column(String, nullable = False)
    description:str = Column(String)

