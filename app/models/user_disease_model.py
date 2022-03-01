from dataclasses import dataclass
from app.configs.database import db
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey


@dataclass
class UserDiseaseModel(db.Model):

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: str = Column(UUID(as_uuid=True),
                          ForeignKey('users.id'), nullable=False)
    disease_id: str = Column(UUID(as_uuid=True),
                             ForeignKey('diseases.id'), nullable=False)
    disease_detail_id: str = Column(
        UUID(as_uuid=True), ForeignKey('diseases_detail.id'), nullable=False)
