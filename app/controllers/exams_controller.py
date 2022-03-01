from http import HTTPStatus
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions.missing_keys import MissingKeysError
from app.models.exam_details_model import ExamDetails
from app.models.exam_model import Exam
from sqlalchemy.orm import Session
from flask import request, jsonify, current_app
from sqlalchemy.exc import IntegrityError, ProgrammingError, DataError
from werkzeug.exceptions import BadRequest, NotFound
from app.models.user_exam_model import UserExam
from app.services.exams_services import find_exam, join_user_exams, verify_exam_key, verify_update_types, verify_user_exam_key


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

        session: Session = current_app.db.session

        verify_user_exam_key(data)

        exam = find_exam(data)
        user_id = get_jwt_identity()["id"]

        data["user_id"] = user_id

        exam_datails = ExamDetails(**data)

        session.add(exam_datails)
        session.commit()

        user_exam = UserExam(user_id=user_id, exam_id=exam.id,
                             exam_details_id=exam_datails.id)

        session.add(user_exam)
        session.commit()
        return jsonify(user_exam), HTTPStatus.CREATED
    except BadRequest:
        return jsonify({"Error": "The keyword 'name' or 'date' does not exit"}), HTTPStatus.BAD_REQUEST


@jwt_required()
def update_exam(exam_id):
    try:
        session: Session = current_app.db.session
        data = request.get_json()

        exam_details_id = UserExam.query.get_or_404(exam_id).id
        exam_details = ExamDetails.query.filter_by(id=exam_details_id).first()

        for key, value in data.items():
            setattr(exam_details, key, value)

        session.add(exam_details)
        session.commit()

        return jsonify(exam_details), HTTPStatus.OK
    except ProgrammingError:
        data = request.get_json()
        msg = verify_update_types(data)
        return jsonify({"Error": msg}), HTTPStatus.BAD_REQUEST
    except (DataError, NotFound):
        return {"Error": f"user_id {exam_id} is not valid"}


@jwt_required()
def delete_user_exam(exam_id):
    try:
        session: Session = current_app.db.session
        exam = UserExam.query.filter_by(
            exam_id=exam_id).first()

        session.delete(exam)
        session.commit()
        return "", HTTPStatus.NO_CONTENT
    except DataError:
        return {"Error": f"user_id {exam_id} is not valid"}, HTTPStatus.NOT_FOUND


@jwt_required()
def get_user_exams():

    user_identity = get_jwt_identity()
    exams_table = UserExam.query.filter_by(
        user_id=user_identity.get("id")).all()
    output = join_user_exams(exams_table)

    return jsonify(output), HTTPStatus.OK
