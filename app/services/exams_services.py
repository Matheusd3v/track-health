from werkzeug.exceptions import BadRequest
from sqlalchemy.orm import Session
from flask import current_app
from app.models.exam_details_model import ExamDetails
from sqlalchemy.orm import Query
from app.models.exam_model import Exam
from app.models.user_exam_model import UserExam


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


def verify_update_types(data):
    response = []
    if data.get("date"):
        if type(data.get("date")) != str:
            msg = "Atribute 'date' is not a valid format"
            response.append(msg)
    if data.get("upload_img"):
        if type(data.get("upload_img")) != str:
            msg = "Atribute 'upload_img' is not a valid format"
            response.append(msg)
    if data.get("description"):
        if type(data.get("description")) != str:
            msg = "Atribute 'description' is not a valid format"
            response.append(msg)
    return response


def join_user_exams(exams_table):
    session = current_app.db.session
    output = []
    for user_exam in exams_table:
        exams: Query = (session.query(
            Exam.name, ExamDetails.date, ExamDetails.upload_img, ExamDetails.description)
            .select_from(UserExam).join(ExamDetails).join(Exam)
            .filter(user_exam.exam_details_id == UserExam.exam_details_id)

        ).all()
        for exam in exams:
            appended_exam = {
                "name": exam[0],
                "date": exam[1],
                "upload_img": exam[2],
                "description": exam[3],
            }
            output.append(appended_exam)
    return output
