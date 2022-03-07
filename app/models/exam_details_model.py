from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Date, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.exam_model import Exam


@dataclass
class ExamDetails(db.Model):

    __tablename__ = "exam_details"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date:str = Column(Date)
    upload_img:str = Column(String)
    description:str = Column(String) 
        
    exam:Exam = relationship("Exam", secondary="user_exam", backref="exams", uselist=False)