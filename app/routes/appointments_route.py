from flask import Blueprint
from app.controllers import appointments_controller

bp_appointments = Blueprint("bp_address", __name__, url_prefix="/appointments")

bp_appointments.post('')(appointments_controller)
bp_appointments.get('')(appointments_controller)
bp_appointments.patch('')(appointments_controller)
bp_appointments.delete('')(appointments_controller)