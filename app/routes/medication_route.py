from flask import Blueprint

from app.controllers.medication_controller import create_medication


bp = Blueprint("bp_medication", __name__, url_prefix="/medication")

bp.post("")(create_medication)