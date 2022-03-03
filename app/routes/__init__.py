from flask import Flask
from app.routes.user_route import bp_user
from app.routes.doctor_route import bp_doctor
from app.routes.anamnesis_route import bp as bp_anamnesis
from app.routes.address_route import bp_address
from app.routes.exams_routes import bp_exam
from app.routes.allergy_route import bp_allergies
from app.routes.medication_route import bp as bp_medication
from app.routes.appointments_route import bp_appointments
from app.routes.surgery_routes import bp as bp_surgery
from app.routes.pdf_anamnesis import bp as bp_pdf

def init_app(app: Flask):
    app.register_blueprint(bp_appointments)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_anamnesis)
    app.register_blueprint(bp_exam)
    app.register_blueprint(bp_address)
    app.register_blueprint(bp_doctor)
    app.register_blueprint(bp_allergies)
    app.register_blueprint(bp_medication)
    app.register_blueprint(bp_surgery)
    app.register_blueprint(bp_pdf)