from app.exceptions.missing_keys import MissingKeysError
from app.models.user_drug_model import UserDrugs
from werkzeug.exceptions import NotFound, Forbidden, BadRequest
from app.services.user_services import remove_space_before_and_after

def drug_data_updated(body: dict, old_data: UserDrugs) -> UserDrugs:
    if not old_data:
        message = {"Error": "Not found this drug data id"}
        raise NotFound(description=message)

    for key, value in body.items():
        if key == "id" or key == "user_id":
            continue
        
        setattr(old_data, key, data_standardized(instance_value=value))
    
    return old_data

def verify_keys_and_values(body: dict):
    required_fields = ["frequency", "description"]
    keys = list(body.keys())

    required_fields.sort()
    keys.sort()

    if not required_fields == keys:
        raise MissingKeysError(required_fields=required_fields)

    verify_values(list(body.values()))

def data_standardized(data: dict = None, instance_value: str = None):

    if data:
        for key, value in data.items():        
            new_value = remove_space_before_and_after(value)
            data.update({key: new_value})
        
        return data        

    new_value = remove_space_before_and_after(instance_value)
    
    return new_value

def verify_values(values: list):
    for value in values:
        if not isinstance(value, str):
            message = {"Error": "All values must be string."}
            raise BadRequest(description=message)

        if not value:
            message = {
                "Error": f"A invalid value has been send. Values: {values}"
            }
            raise BadRequest(description=message)




