from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Surgery(db.Model):

    __tablename__="surgerys"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name:str = Column(String, nullable = False, unique = True)



def asdict(self):
    return asdict(self)