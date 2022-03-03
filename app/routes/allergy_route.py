from flask import Blueprint
from app.controllers.allergies_controller import create_allergies, get_allergies, delete_allergy, update_allergy

bp_allergies = Blueprint("bp_allergies", __name__, url_prefix="/allergies")

bp_allergies.post("")(create_allergies)

bp_allergies.get("")(get_allergies)

bp_allergies.patch("/<allergy_id>")(update_allergy)

bp_allergies.delete("/<allergy_id>")(delete_allergy)