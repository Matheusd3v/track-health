from http import HTTPStatus
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import null
from app.models.exam_details_model import ExamDetails
from app.models.user_exam_model import UserExam
from sqlalchemy.orm import Session
from flask import request, current_app
from werkzeug.exceptions import BadRequest, NotFound
from app.services.exam_files_services import get_key_file, upload_file
from botocore.exceptions import NoCredentialsError, ClientError

from app.services.profile_image_services import delete_object_from_cloud

@jwt_required()
def upload_exam_file(exam_id: str):
    try:
        session: Session = current_app.db.session
        
        if not exam_id:
            message = {"Error": "Exam_id not has been send."}
            raise NotFound(description=message)

        user_exam = session.query(UserExam).filter_by(exam_id = exam_id).first()

        if not user_exam:
            message = {"Error": f"Not found exam."}
            raise NotFound(description=message)

        exam_details = session.query(ExamDetails).get(user_exam.exam_details_id)

        file_name = list(request.files)[0]
        data = request.files[f"{file_name}"]

        url = upload_file(data)

        exam_details.upload_img = url

        session.add(exam_details)
        session.commit()
        
        return {"success": url}, HTTPStatus.CREATED
    
    except BadRequest as e:
        return e.description, e.code

    except NotFound as e:
        return e.description, e.code

    except NoCredentialsError as e:
        return {"Error": e.fmt}, HTTPStatus.INTERNAL_SERVER_ERROR

    except ClientError as e:
        message = {"ClientError": e.response["Error"]["Code"]}
        return message, HTTPStatus.BAD_REQUEST

@jwt_required()
def delete_exam_file(exam_id: str):
    try: 
        session: Session = current_app.db.session

        if not exam_id:
            message = {"Error": "Exam_details_id not has been send."}
            raise NotFound(description=message)

        user_exam = session.query(UserExam).filter_by(exam_id = exam_id).first()

        if not user_exam:
            message = {"Error": f"Not found exam."}
            raise NotFound(description=message)

        exam_details = session.query(ExamDetails).get(user_exam.exam_details_id)

        file_key = get_key_file(exam_details.upload_img)

        delete_object_from_cloud(file_key)

        exam_details.upload_img = None

        session.add(exam_details)
        session.commit()

        return "", HTTPStatus.NO_CONTENT

    except BadRequest as e:
        return e.description, e.code

    except NotFound as e:
        e.description, e.code

    
