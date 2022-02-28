from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Boolean, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

 
@dataclass
class Anamnesis(db.Model):

        __tablename__="anamnesis"

        id:str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
        diseases:bool = Column(Boolean, nullable = False)
        allergy:bool = Column(Boolean, nullable = False)
        continous_medication:bool = Column(Boolean, nullable = False)
        surgery:bool = Column(Boolean, nullable = False)
        alcoholic:bool = Column(Boolean, nullable = False)
        drug_user:bool = Column(Boolean, nullable = False)
        smoker:bool = Column(Boolean, nullable = False)
        physical_activity:bool = Column(Boolean, nullable = False)
        diabetes:bool = Column(Boolean, nullable = False)
        hipertension:bool = Column(Boolean, nullable = False)

        user_id: str = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)
