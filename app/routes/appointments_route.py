from flask import Blueprint
from app.controllers import appointments_controller

bp_appointments = Blueprint("bp_appointments", __name__, url_prefix="/appointments")

bp_appointments.post('')(appointments_controller.create_controller)
bp_appointments.get('')(appointments_controller.get_appointment)
bp_appointments.patch('')(appointments_controller.patch_appointment)
bp_appointments.delete('')(appointments_controller.delete_appointment)