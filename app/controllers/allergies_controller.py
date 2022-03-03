from http.client import BAD_REQUEST
from flask import request, jsonify, current_app
from sqlalchemy.orm import Session
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from werkzeug.exceptions import NotFound
from app.exceptions.missing_keys import MissingKeysError
from werkzeug.exceptions import BadRequest


from app.models.user_allergies_model import UserAllergyModel
from app.models.allergies_model import AllergyModel
from app.services.allergy_services import verify_fields_and_values


@jwt_required()
def create_allergies():
    try:
        session: Session = current_app.db.session
        data = request.get_json()
        user_jwt = get_jwt_identity()

        verify_fields_and_values(data)

        data['user_id'] = user_jwt['id']

        allergies = AllergyModel.query.all()

        allergies_name = []
        for allergy in allergies:
            allergies_name.append(allergy.name)

        if not data['name'] in allergies_name:
            new_allergy = AllergyModel(name = data['name'])
            session.add(new_allergy)
            session.commit()

        new_allergy = AllergyModel.query.filter_by(name = data['name']).first()

        data['allergy_id'] = new_allergy.id

        data.pop('name')

        allergy = UserAllergyModel(**data)

        session.add(allergy)
        session.commit()

        return jsonify(allergy), HTTPStatus.CREATED

    except MissingKeysError as e:
        return e.message(), e.status_code

    except BadRequest as e:
        return e.description, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_allergies():
    session: Session = current_app.db.session
    user_jwt = get_jwt_identity()

    my_allergies = session.query(UserAllergyModel).filter_by(user_id = user_jwt["id"]).all()

    return jsonify(my_allergies), HTTPStatus.OK


@jwt_required()
def update_allergy(allergy_id):
    try:
        session: Session = current_app.db.session

        data = request.get_json()

        verify_fields_and_values(data)

        the_allergy = session.query(UserAllergyModel).get(allergy_id)

        if 'name' in data.keys():
            print('*' * 20)
            allergies = AllergyModel.query.all()

            allergies_name = []
            for allergy in allergies:
                allergies_name.append(allergy.name)

            if not data['name'] in allergies_name:
                new_allergy = AllergyModel(name = data['name'])
                session.add(new_allergy)
                session.commit()

            new_allergy = AllergyModel.query.filter_by(name = data['name']).first()

            data['allergy_id'] = new_allergy.id

        for key, value in data.items():
            setattr(the_allergy, key, value)

        session.add(the_allergy)
        session.commit()

        return jsonify(the_allergy), HTTPStatus.OK
    
    except NotFound as e:
        return e.description, e.code

    except MissingKeysError as e:
        return e.message(), e.status_code

    except BadRequest as e:
        return e.description, HTTPStatus.BAD_REQUEST

@jwt_required()
def delete_allergy(allergy_id):
    try:
        session: Session = current_app.db.session

        allergy = session.query(UserAllergyModel).get(allergy_id)

        session.delete(allergy)
        session.commit()

        return '', HTTPStatus.NO_CONTENT
    
    except NotFound as e:
        return e.description, e.code