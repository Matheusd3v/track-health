from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Date
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.surgery_model import Surgery

@dataclass
class SurgeryDetails(db.Model):

    __tablename__ = "surgerys_details"
    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date:str = Column(Date, nullable = False)
    description:str = Column(String)    

    surgery_name:Surgery = relationship("Surgery",
            secondary="user_surgery",
            backref="surgery_details", uselist=False)    
