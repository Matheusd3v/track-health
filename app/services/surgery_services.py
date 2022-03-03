from werkzeug.exceptions import BadRequest

def validate_body_surgery(data):
    
    valid_field = ["name"]

    for key in data.keys():
        if key not in valid_field:
            raise BadRequest

    return 'validate_body'


def validate_body_surgery_details(data):
    
    valid_field = ["name","date", "description"]
    required_field = ["name","date"]

    if "name" not in data or "date" not in data:
        raise BadRequest

    for key in data.keys():
        if key not in valid_field:
            raise BadRequest

    return 'validate_body'


def update_surgery(data, updated_surgery):

    allowed_fields = ["date", "description"]

    for key, value in data.items():
        if key in allowed_fields:
            setattr(updated_surgery, key, value)



def serializing_surgery(user):
    surgerys = user["surgerys"]

    all_surgerys = []
    for surgery in surgerys:
        surgery = {
            "id":surgery["surgery_name"]["id"],
            "name":surgery["surgery_name"]["name"],
            "description":surgery["description"],
            "date":surgery["date"]
        }
        all_surgerys.append(surgery)

    return all_surgerys