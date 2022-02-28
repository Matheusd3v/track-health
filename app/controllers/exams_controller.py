from http import HTTPStatus
from flask import request
from flask_jwt_extended import jwt_required
from app.exceptions.missing_keys import MissingKeysError
from app.models.exam_model import Exam
from sqlalchemy.orm import Session
from flask import request, jsonify, current_app
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from app.services.exams_services import verify_exam_key

@jwt_required()
def create_exams():
    try:
        data = request.get_json()
        verify_exam_key(data)

        session: Session = current_app.db.session
        exam = Exam(**data)
        session.add(exam)
        session.commit()
        return jsonify(exam), HTTPStatus.CREATED

    except IntegrityError:
        return jsonify({"Error": "The exam name already exists."}), HTTPStatus.CONFLICT
    except BadRequest:
        return jsonify({"Error": "The keyword 'name' does not exit"}), HTTPStatus.BAD_REQUEST