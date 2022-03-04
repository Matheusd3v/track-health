from flask import Blueprint
from app.controllers.allergies_controller import create_new_allergy

bp_allergies = Blueprint("bp_allergies", __name__, url_prefix="/allergy")

bp_allergies.post("")(create_new_allergy)

