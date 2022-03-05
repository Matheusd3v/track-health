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
import logging

@jwt_required()
def upload_image():
    try:
        session: Session = current_app.db.session
        user_id = get_jwt_identity()["id"]

        file_name = list(request.files)[0]
        data = request.files[f"{file_name}"]
        print(data.name, "*"*50)

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
        logging.error(e)
        message = {"Error": ""}
        return e.MSG_TEMPLATE, HTTPStatus.BAD_REQUEST
        
    except BadRequest as e:
        return e.description, e.code
    
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            message = {"Error": "User already have a image profile."}
            return message, HTTPStatus.CONFLICT


@jwt_required()
def delete_image_profile():
    session: Session = current_app.db.session
    user_id = get_jwt_identity()["id"]

    image = session.query(ProfileImageModel).filter_by(user_id=user_id).first()
    image_id = image.id

    delete_object_from_cloud(image_id)

    session.delete(image)
    session.commit()

    return "", HTTPStatus.NO_CONTENT






    
    


    
