from werkzeug.exceptions import BadRequest
from sqlalchemy.orm import Session
from flask import current_app
from app.models.diseases_detail_model import DiseasesDetailModel
from app.models.diseases_model import DiseasesModel
from sqlalchemy.orm import Query

from app.models.user_disease_model import UserDiseaseModel


def verify_user_diseases_key(data: dict):

    if not data.get("name"):
        raise BadRequest


def find_diseases(data: dict):
    diseases_name = data.get("name")
    session: Session = current_app.db.session

    diseases = session.query(DiseasesModel).filter_by(
        name=diseases_name).first()

    if not diseases:
        diseases = DiseasesModel(name=diseases_name)
        session.add(diseases)
        session.commit()
    return diseases


def verify_update_types(data):
    response = []
    if data.get("name"):
        if type(data.get("name")) != str:
            msg = "Atribute 'name' is not a valid format"
            response.append(msg)
    if data.get("medication"):
        if type(data.get("medication")) != str:
            msg = "Atribute 'medication' is not a valid format"
            response.append(msg)
    if data.get("description"):
        if type(data.get("description")) != str:
            msg = "Atribute 'description' is not a valid format"
            response.append(msg)
    return response


def normalize_disease_keys(data: dict) -> dict:
    if data.get("name"):
        name = data.pop("name").title()
        data["name"] = name
    if data.get("description"):
        description = data.pop("description").capitalize()
        data["description"] = description
    if data.get("medication"):
        medication = data.pop("medication").title()
        data["medication"] = medication
    return data


def serializing_all_fields(user_disease):
    diseases = user_disease['diseases']
    for disease in diseases:
        name = disease['disease']['name']
        disease['name'] = name
        disease.pop('disease')
    print(user_disease)
    return user_disease


def join_user_disease(disease_table):
    session = current_app.db.session
    output = []
    for user_disease in disease_table:
        diseases: Query = (session.query(DiseasesModel.id,
                                         DiseasesModel.name, DiseasesDetailModel.description, DiseasesDetailModel.medication)
                           .select_from(UserDiseaseModel).join(DiseasesDetailModel).join(DiseasesModel)
                           .filter(user_disease.disease_detail_id == UserDiseaseModel.disease_detail_id)

                           ).all()
        for disease in diseases:
            appended_disease = {
                "id": disease[0],
                "name": disease[1],
                "description": disease[2],
                "medication": disease[3],
            }
            output.append(appended_disease)
    return output
