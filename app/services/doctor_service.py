from app.exceptions.missing_keys import MissingKeysError
from werkzeug.exceptions import BadRequest
from http import HTTPStatus
import re

def verify_fields_and_values(body: dict):
    required_fields = [ "name", "type", "email", "phone", "user_id", "address_id"]

    for key in body.keys():
        if not key in required_fields:
            raise MissingKeysError(required_fields, list(body.keys()))
    
    verify_values(list(body.values()))


def verify_values(values: list):
    for value in values:
        if not isinstance(value, str):
            message = {"Error": "All values must be string."}
            raise BadRequest(description=message)

