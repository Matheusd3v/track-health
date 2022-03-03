from email import message
from app.models.user_drug_model import UserDrugs
from werkzeug.exceptions import NotFound

def drug_data_updated(body: dict, old_data: UserDrugs) -> UserDrugs:
    if not old_data:
        message = {"Error": "Not found this drug data id"}
        raise NotFound(description=message)

    for key, value in body.items():
        if key == "id" or key == "user_id":
            continue
        
        setattr(old_data, key, value)
    
    return old_data