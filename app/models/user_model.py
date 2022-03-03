from sqlalchemy import Column, String, Date
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

from app.models.allergies_model import AllergyModel
from app.models.surgery_details_model import SurgeryDetails
from app.models.user_smoker_model import UserSmoker
from app.models.user_physical_activity_model import UserPhysicalActivity
@dataclass
class User(db.Model):
    __tablename__ = "users"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: str = Column(String(100), nullable=False)
    email: str = Column(String(150), nullable=False, unique=True)
    birth_date: str = Column(Date, nullable=False)
    password_hash = Column(String, nullable=False)
    gender: str = Column(String(50))
    sex: str = Column(String(50))
    image = Column(String)

    allergy:AllergyModel = relationship("AllergyModel",
            secondary="user_allergies",
            backref='user')

    surgerys:SurgeryDetails = relationship("SurgeryDetails",
            secondary="user_surgery",
            backref='user')    


    user_drug: str = relationship("UserDrugs", 
            backref="user_drug", uselist=False, viewonly=True)
      
    smoker: UserSmoker = relationship("UserSmoker",
            backref = 'user_smoker', uselist = False) 
    
    physical_activity: UserPhysicalActivity = relationship("UserPhysicalActivity",
            backref = 'physical_activity', uselist = False) 


    @property
    def password(self):
        raise AttributeError("Access not allowed for reading.")
    
    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)