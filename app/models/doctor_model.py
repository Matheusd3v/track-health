from sqlalchemy import Column, ForeignKey, String
from app.configs.database import db
from dataclasses import dataclass, asdict
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.models.address_model import AddressModel
from sqlalchemy.orm import relationship


@dataclass
class DoctorModel(db.Model):

    __tablename__ = "doctors"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: str = Column(String(100), nullable=False)
    type: str = Column(String(50), nullable=False)
    email: str = Column(String(50))
    phone: str = Column(String(50), nullable=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False)

    address_id = Column(UUID(as_uuid=True), ForeignKey('address.id'), nullable=False)

    address: AddressModel = relationship("AddressModel", uselist=False, 
        backref="doctor", viewonly=True)

    
    def asdict(self):
        return asdict(self)