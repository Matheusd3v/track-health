from app.exceptions.missing_keys import MissingKeysError
from werkzeug.exceptions import BadRequest

def verify_fields_and_values(body: dict):
    required_fields = [ "name", "type", "user_id", "phone", "address_id"]
    allowed_fields = ["email"]

    for key in body.keys():
        if not key in required_fields and key not in allowed_fields:
            raise MissingKeysError(required_fields, list(body.keys()))

    for key in required_fields:
        if not key in body.keys():
            raise MissingKeysError(required_fields, list(body.keys()))

    verify_values(list(body.values()))


def verify_values(values: list):
    for value in values:
        if not isinstance(value, str):
            message = {"Error": "All values must be string."}
            raise BadRequest(description=message)


def remove_spaces(value: str) -> str:
    value_list = value.split()
    value_list[0] = value_list[0].capitalize()
    new_value = " ".join(value_list)
    
    return new_value