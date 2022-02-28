from flask import Blueprint

from app.controllers.exams_controller import create_exams

bp_exam = Blueprint("bp_exam", __name__, url_prefix="/exams")

bp_exam.post("")(create_exams)