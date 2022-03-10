from flask import request, jsonify, current_app
from sqlalchemy.orm import Session
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import DataError, IntegrityError
from app.exceptions.missing_keys import MissingKeysError
from werkzeug.exceptions import BadRequest

from app.models.user_allergies_model import UserAllergyModel
from app.models.allergies_model import AllergyModel
from app.services.allergy_services import verify_fields_and_values, remove_spaces


@jwt_required()
def create_allergies():
    try:
        session: Session = current_app.db.session
        data = request.get_json()
        user_jwt = get_jwt_identity()

        verify_fields_and_values(data)

        data['name'] = data['name'].title()
        data['description'] = remove_spaces(data['description'])

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

        my_allergies = session.query(UserAllergyModel).filter_by(user_id = data['user_id']).all()
        my_allergies_name = [allergy.allergy.name for allergy in my_allergies]
        if data['name'] in my_allergies_name:
            return {"error": "allergy already added"}, HTTPStatus.CONFLICT

        data['allergy_id'] = new_allergy.id

        data.pop('name')

        allergy = UserAllergyModel(**data)

        session.add(allergy)
        session.commit()

        allergy = allergy.asdict()
        name = allergy['allergy']['name']
        allergy['name'] = name
        allergy.pop('allergy')

        return jsonify(allergy), HTTPStatus.CREATED

    except MissingKeysError as e:
        return e.message(), e.status_code

    except BadRequest as e:
        return e.description, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        return {"error": "Allergy already created"}, HTTPStatus.CONFLICT


@jwt_required()
def get_allergies():
    session: Session = current_app.db.session
    user_jwt = get_jwt_identity()

    my_allergies = session.query(UserAllergyModel).filter_by(user_id = user_jwt["id"]).all()

    output = []
    for allergy in my_allergies:
        allergy = allergy.asdict()
        name = allergy['allergy']['name']
        allergy['name'] = name
        allergy.pop('allergy')
        output.append(allergy)

    return jsonify(output), HTTPStatus.OK


@jwt_required()
def update_allergy(allergy_id):
    try:
        session: Session = current_app.db.session

        data = request.get_json()

        verify_fields_and_values(data)

        the_allergy = session.query(UserAllergyModel).get_or_404(allergy_id)

        if data.get('description'):
            data['description'] = remove_spaces(data['description'])

        if 'name' in data.keys():
            data['name'] = data['name'].title()
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

        
        the_allergy = the_allergy.asdict()
        name = the_allergy['allergy']['name']
        the_allergy['name'] = name
        the_allergy.pop('allergy')

        return jsonify(the_allergy), HTTPStatus.OK
    
    except DataError as e:
        return {"error": "wrong id"}, e.code
    
    except NotFound as e:
        return {"error": f"{e.description}"}, e.code

    except MissingKeysError as e:
        return e.message(), e.status_code

    except BadRequest as e:
        return e.description, HTTPStatus.BAD_REQUEST

@jwt_required()
def delete_allergy(allergy_id):
    try:
        session: Session = current_app.db.session

        allergy = session.query(UserAllergyModel).get_or_404(allergy_id)

        session.delete(allergy)
        session.commit()

        return '', HTTPStatus.NO_CONTENT

    except DataError as e:
        return {"error": "wrong id"}, e.code
    
    except NotFound as e:
        return {"error": f"{e.description}"}, e.code


def create_new_allergy():
    try:
        session: Session = current_app.db.session
        data = request.get_json()

        verify_fields_and_values(data)

        data['name'] = data['name'].title()

        allergy = AllergyModel(**data)

        session.add(allergy)
        session.commit()

        return jsonify(allergy), HTTPStatus.CREATED

    except MissingKeysError as e:
        return e.message(), e.status_code

    except BadRequest as e:
        return e.description, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        return {"error": "Allergy already created"}, HTTPStatus.CONFLICT


