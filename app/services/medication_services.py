from werkzeug.exceptions import BadRequest

from app.models.medication_model import Medication
from app.models.user_medication import UserMedication


def validate_body(data):
    required_fields = ["name"]
    allowed_fields = ["description"]
    for key in data.keys():
        if key not in required_fields and key not in allowed_fields:
            raise BadRequest(description="The only fields alloweds its ['name','allowed_fields'] ")


def validate_update(data, medication_detail):
    valid_fields = ["description"]

    for key,value in data.items():
        if key in valid_fields:
            setattr(medication_detail, key, value)


def serializing_medications(user):

    user = user.asdict()
    medications = []
    for medication  in user["medications"]:
        medication_details =medication.pop("medication")    
        medication.pop("user_id")
        medication["name"] = medication_details["name"]
        medications.append(medication)

        
    return medications