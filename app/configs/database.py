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
    from app.models.surgery_model import Surgery
    from app.models.surgery_details_model import SurgeryDetails
    from app.models.user_surgery_model import UserSurgery
    from app.models.user_physical_activity_model import UserPhysicalActivity
    from app.models.user_smoker_model import UserSmoker
