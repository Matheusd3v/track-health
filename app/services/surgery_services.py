from werkzeug.exceptions import BadRequest

def validate_body_surgery(data):
    
    valid_field = ["name"]

    for key in data.keys():
        if key not in valid_field:
            raise BadRequest

    return 'validate_body'


def validate_body_surgery_details(data):
    
    valid_field = ["name","date", "description"]

    for key in data.keys():
        if key not in valid_field:
            raise BadRequest

    return 'validate_body'