from flask import Flask
from app.routes.user_route import bp_user
from app.routes.doctor_route import bp_doctor
from app.routes.anamnesis_route import bp as bp_anamnesis
from app.routes.address_route import bp_address
from app.routes.exams_routes import bp_exam
from app.routes.allergy_route import bp_allergies

def init_app(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_anamnesis)
    app.register_blueprint(bp_exam)
    app.register_blueprint(bp_address)
    app.register_blueprint(bp_doctor)
    app.register_blueprint(bp_allergies)

