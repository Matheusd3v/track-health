from flask import jsonify
from app.models.user_model import User


def get_anamnesis(user_id):
    user = User.query.filter_by(id = user_id).first()
    user = user.asdict()
    user["anamnesis"][0].pop("user_id")
    return user["anamnesis"]
    