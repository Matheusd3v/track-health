from http import HTTPStatus
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions.missing_keys import MissingKeysError
from app.models.exam_details_model import ExamDetails
from app.models.exam_model import Exam
from sqlalchemy.orm import Session
from flask import request, jsonify, current_app
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from app.models.user_exam_model import UserExam
from app.services.exams_services import find_exam, verify_exam_key, verify_user_exam_key


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


@jwt_required()
def create_user_exam():
    try:
        data = request.get_json()
        verify_user_exam_key(data)
        session: Session = current_app.db.session
        exam = find_exam(data)[0]

        user_id = get_jwt_identity()["id"]
        exam_datails = ExamDetails(user_id=user_id, date=data.get("date"))
        session.add(exam_datails)
        session.commit()
        user_exam = UserExam(user_id=user_id, exam_id=exam.id,
                             exam_details_id=exam_datails.id)
        session.add(user_exam)
        session.commit()
        return jsonify(user_exam), HTTPStatus.CREATED
    except BadRequest:
        return jsonify({"Error": "The keyword 'name' or 'date' does not exit"}), HTTPStatus.BAD_REQUEST
