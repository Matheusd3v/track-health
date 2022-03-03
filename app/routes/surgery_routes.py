from flask import Blueprint
from app.controllers.surgery_controller import create_surgery


bp = Blueprint("bp_surgery", __name__, url_prefix="/surgery")

bp.post("")(create_surgery)