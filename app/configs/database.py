from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_app(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.db = db

    from app.models.doctor_model import DoctorModel
    from app.models.user_model import User
    from app.models.anamnesis_model import Anamnesis
    from app.models.appointment_model import AppointmentModel
    from app.models.exam_model import Exam
    from app.models.exam_details_model import ExamDetails
    from app.models.address_model import AddressModel
    from app.models.user_exam_model import UserExam
    from app.models.allergies_model import AllergyModel
    from app.models.user_allergies_model import UserAllergyModel

