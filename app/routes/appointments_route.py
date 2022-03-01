from flask import Blueprint
from app.controllers import appointments_controller

bp_appointments = Blueprint("bp_appointments", __name__, url_prefix="/appointments")

bp_appointments.post('')(appointments_controller.create_controller)
