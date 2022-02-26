from app.models.user_model import User
from werkzeug.exceptions import NotFound












def user_updated(body: dict, old_user: User ):
    allowed_keys = list(old_user.__dict__.keys())

    if not old_user:
        raise NotFound(description={"msg": "User not found!"})

    for key, value in body.items():
        if key == "id":
            continue

        if key in allowed_keys:
            setattr(old_user, key, value)
    
    return old_user