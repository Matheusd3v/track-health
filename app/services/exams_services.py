from werkzeug.exceptions import BadRequest
from sqlalchemy.orm import Session
from flask import current_app

from app.models.exam_model import Exam


def verify_exam_key(data: dict):

    if not data.get("name"):
        raise BadRequest


def find_exam(data: dict):
    exam_name = data.get("name")
    session: Session = current_app.db.session
    exam = session.query(Exam).filter_by(name=exam_name).all()
    return exam


def verify_user_exam_key(data: dict):

    if not data.get("name") or not data.get("date"):
        raise BadRequest
