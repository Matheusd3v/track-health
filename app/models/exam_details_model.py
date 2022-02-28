from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Date, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID



@dataclass
class ExamDetails(db.Model):

    __tablename__ = "exam_details"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date:str = Column(Date)
    upload_img:str = Column(String)
    description:str = Column(String) 
        
    user_id: str = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)
