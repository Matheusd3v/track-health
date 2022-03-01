from app.configs.database import db
from sqlalchemy import Column, String, Date
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class SurgeryDetails(db.Model):

    __tablename__ = "surgerys_details"
    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date:str = Column(Date, nullable = False)
    description:str = Column(String)    

