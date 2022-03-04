from dataclasses import dataclass
from app.configs.database import db
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey


@dataclass
class UserExam(db.Model):
    __tablename__ = "user_exam"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: str = Column(UUID(as_uuid=True),
                          ForeignKey('users.id'), nullable=False)
    exam_id: str = Column(UUID(as_uuid=True),
                          ForeignKey('exams.id'), nullable=False)
    exam_details_id: str = Column(
        UUID(as_uuid=True), ForeignKey('exam_details.id'), nullable=False)
