from sqlalchemy import Column, String, Date
from app.configs.database import db
from dataclasses import asdict, dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

from app.models.allergies_model import AllergyModel
from app.models.anamnesis_model import Anamnesis
from app.models.exam_details_model import ExamDetails
from app.models.exam_model import Exam
from app.models.medication_model import Medication
from app.models.surgery_details_model import SurgeryDetails
from app.models.user_alcoholic_model import UserAlcoholic
from app.models.user_smoker_model import UserSmoker
from app.models.user_physical_activity_model import UserPhysicalActivity
from app.models.diseases_detail_model import DiseasesDetailModel


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

    allergy: AllergyModel = relationship("AllergyModel",
            secondary = "user_allergies",
            backref = 'user',
            viewonly = True)

    medications: Medication = relationship("UserMedication", 
            backref = "medication_user", 
            viewonly = True)

    surgerys: SurgeryDetails = relationship("SurgeryDetails",
            secondary = "user_surgery",
            backref = 'user',
            viewonly = True) 

    alcohol: UserAlcoholic = relationship("UserAlcoholic",
            backref = 'user_alcoholic', 
            uselist = False, 
            viewonly = True)

    user_drug: str = relationship("UserDrugs", 
            backref = "user_drug", 
            uselist = False, 
            viewonly = True)
      
    smoker: UserSmoker = relationship("UserSmoker",
            backref = 'user_smoker', 
            uselist = False, 
            viewonly = True) 
      
    physical_activity: UserPhysicalActivity = relationship("UserPhysicalActivity",
            backref = 'physical_activity', 
            uselist = False, 
            viewonly = True) 


    anamnesis:Anamnesis = relationship("Anamnesis", 
            backref = "anamnesis_user", 
            viewonly = True)

    diseases:DiseasesDetailModel = relationship("DiseasesDetailModel",
            secondary = "user_diseases",
            backref = 'user', 
            viewonly = True)
      
    exams:ExamDetails = relationship("ExamDetails", 
            secondary = "user_exam", 
            backref = "exams_user", 
            viewonly = True)

    @property
    def password(self):
        raise AttributeError("Access not allowed for reading.")
    
    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    
    def asdict(self):
        return asdict(self)
