from flask import Blueprint
from app.controllers.doctor_controller import create_doctor, delete_doctor, get_doctor, update_doctor

bp_doctor = Blueprint("bp_doctor", __name__, url_prefix="/doctor")

bp_doctor.post("")(create_doctor)

bp_doctor.get("")(get_doctor)

bp_doctor.patch("<doctor_id>")(update_doctor)

bp_doctor.delete("<doctor_id>")(delete_doctor)