from werkzeug.exceptions import BadRequest
def verify_exam_key(data:dict):
    
    if not data.get("name"):
            raise BadRequest