from dataclasses import dataclass, asdict
from app.configs.database import db
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from app.models.diseases_detail_model import DiseasesDetailModel

from app.models.diseases_model import DiseasesModel


@dataclass
class UserDiseaseModel(db.Model):
    __tablename__ = "user_diseases"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    user_id: str = Column(UUID(as_uuid=True),
                          ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    disease_id: str = Column(UUID(as_uuid=True),
                             ForeignKey('diseases.id'), nullable=False)
    disease_detail_id: str = Column(UUID(as_uuid=True),
                                    ForeignKey('diseases_detail.id'), nullable=False)

    disease_details: DiseasesDetailModel = relationship(
        "DiseasesDetailModel", backref="user_id")

    def asdict(self):
        return asdict(self)
