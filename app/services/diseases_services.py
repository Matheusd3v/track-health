from werkzeug.exceptions import BadRequest
from sqlalchemy.orm import Session
from flask import request, jsonify, current_app

from app.models.diseases_model import DiseasesModel


def verify_user_diseases_key(data: dict):

    if not data.get("name"):
        raise BadRequest


def find_diseases(data: dict):
    diseases_name = data.get("name")
    session: Session = current_app.db.session

    diseases = session.query(DiseasesModel).filter_by(
        name=diseases_name).first()

    if not diseases:
        diseases = DiseasesModel(name=diseases_name)
        session.add(diseases)
        session.commit()
    return diseases
