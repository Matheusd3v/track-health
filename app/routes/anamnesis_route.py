from flask import Blueprint
from app.controllers.anamnesis_controller import create_anamnesis, update_anamnesis


bp = Blueprint("bp_anamnesis", __name__, url_prefix="/user")

bp.post("/anamnesis")(create_anamnesis)
bp.patch("/anamnesis")(update_anamnesis)