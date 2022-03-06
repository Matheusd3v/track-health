from cProfile import Profile
from email import message
from flask import request, jsonify, current_app
from app.models.profile_image_model import ProfileImageModel
from http import HTTPStatus
from sqlalchemy.orm import Session
from werkzeug.exceptions import BadRequest, NotFound, Forbidden
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from flask_jwt_extended import jwt_required, get_jwt_identity
from botocore.exceptions import NoCredentialsError, ClientError
from app.services.profile_image_services import delete_object_from_cloud, upload_and_get_url, verify_names

@jwt_required()
def upload_image():
    try:
        session: Session = current_app.db.session
        user_id = get_jwt_identity()["id"]

        if not list(request.files):
            message = {"Error": "No files were sent."}
            raise BadRequest(description=message)

        file_name = list(request.files)[0] 
        data = request.files[f"{file_name}"]

        url, id = upload_and_get_url(data)
        name = verify_names(data)

        profile_image = ProfileImageModel(
            id = id,
            user_id = user_id,
            name = name,
            url = url
        )

        session.add(profile_image)
        session.commit()

        return jsonify(profile_image), HTTPStatus.CREATED

    except NoCredentialsError as e:
        return {"Error": e.fmt}, HTTPStatus.INTERNAL_SERVER_ERROR

    except ClientError as e:
        message = {"ClientError": e.response["Error"]["Code"]}
        return message, HTTPStatus.BAD_REQUEST
        
    except BadRequest as e:
        return e.description, e.code
    
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            message = {"Error": "User already have a image profile."}
            return message, HTTPStatus.CONFLICT


@jwt_required()
def get_image_profile():
    try:
        session: Session = current_app.db.session
        id_user = get_jwt_identity()["id"]

        image_profile = session.query(ProfileImageModel).filter_by(user_id = id_user).first()

        if not image_profile:
            message = {"Error": "User don't have image profile."}
            raise NotFound(description=message)

        return jsonify(image_profile), HTTPStatus.OK

    except NotFound as e:
        return e.description, e.code


@jwt_required()
def delete_image_profile():
    try:
        session: Session = current_app.db.session
        user_id = get_jwt_identity()["id"]

        image = session.query(ProfileImageModel).filter_by(user_id=user_id).first()

        if not image:
            message = {"Error": "User don't have image profile."}
            raise NotFound(description=message)

        image_id = image.id

        delete_object_from_cloud(image_id)

        session.delete(image)
        session.commit()

        return "", HTTPStatus.NO_CONTENT
    
    except NotFound as e:
        return e.description, e.code






    
    


    
