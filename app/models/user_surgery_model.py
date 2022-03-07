from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Date, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class UserSurgery(db.Model):

    __tablename__ = "user_surgery"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: str = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete="CASCADE"), nullable = False)
    surgery_id:str = Column(UUID(as_uuid=True), ForeignKey("surgerys.id"), nullable = False)
    surgery_detail_id:str = Column(UUID(as_uuid=True), ForeignKey("surgerys_details.id"))
