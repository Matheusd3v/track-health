from werkzeug.exceptions import BadRequest


def validate_body(data):
    required_fields = ["name"]
    allowed_fields = ["description"]
    for key in data.keys():
        if key not in required_fields and key not in allowed_fields:
            raise BadRequest(description="The only fields alloweds its ['name','allowed_fields'] ")