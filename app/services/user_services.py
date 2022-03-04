from app.exceptions.missing_keys import MissingKeysError
from app.models.user_model import User
from werkzeug.exceptions import NotFound, BadRequest, Unauthorized

def verify_fields_and_values(body: dict):
    required_fields = [ "name", "email", "birth_date", "password"]
    allowed_fields = ["sex", "gender", "image"]
    for key in body.keys():
        if not key in required_fields and key not in allowed_fields:
            raise MissingKeysError(required_fields, list(body.keys()))
    
    verify_values(list(body.values()))

def verify_values(values: list):
    for value in values:
        if not isinstance(value, str):
            message = {"Error": "All values must be string."}
            raise BadRequest(description=message)

def verify_user(user):
    if not user:
        message = {"Error": "User not found."}
        raise NotFound(description=message)

def verify_user_and_password(user: User, password: str):
    verify_user(user)
    
    if not user.check_password(password):
        message = {"Error": "Email and password don't match."}
        raise Unauthorized(description=message)

def user_updated(body: dict, old_user: User ) -> User:
    verify_user(old_user)
    verify_values(list(body.values()))

    allowed_keys = [
        "name",	"email", "birth_date", "password", "gender", "sex", "password"
    ]

    for key, value in body.items():
        if key == "id":
            continue

        if key in allowed_keys:
            setattr(old_user, key, data_normalized(instance_key=key, instance_value=value))
    
    return old_user

def data_normalized(data: dict = None, instance_value: str = None, instance_key: str = None) -> dict:
    standard_keys = ["name", "sex", "gender"]

    if data:
        for key, value in data.items():        
            if key == "email":
                new_value = remove_space_before_and_after(value)
                new_value = new_value.lower()
                data.update({key: new_value})

            if key == "gender" or key == "sex" or key == "name":
                new_value = remove_space_before_and_after(value)
                new_value = new_value.title()
                data.update({key: new_value})
        
        return data        

    if instance_key in standard_keys:
        new_value = remove_space_before_and_after(instance_value)
        new_value = new_value.title()

        return new_value

    if instance_key == "email":
        new_value = remove_space_before_and_after(instance_value)
        new_value = new_value.lower()

        return new_value
    
    return instance_value

def remove_space_before_and_after(text: str) -> str:
    text_list = text.split()

    return " ".join(text_list)
