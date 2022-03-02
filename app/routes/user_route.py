from flask import Blueprint
from app.controllers.diseases_controller import create_user_diseases, update_diseases, delete_user_diseases, get_user_diseases
from app.controllers.exams_controller import create_user_exam, delete_user_exam, get_user_exams, update_exam
from app.controllers.user_controller import create_user, delete_user, get_user, login, update_user

bp_user = Blueprint("bp_user", __name__, url_prefix="/user")

bp_user.post("/register")(create_user)

bp_user.post("/login")(login)

bp_user.get("")(get_user)

bp_user.patch("")(update_user)

bp_user.delete("")(delete_user)

bp_user.get("/exam")(get_user_exams)

bp_user.post("/exam")(create_user_exam)

bp_user.patch("/exam/<exam_id>")(update_exam)

bp_user.delete("/exam/<exam_id>")(delete_user_exam)

bp_user.get("/diseases")(get_user_diseases)

bp_user.post("/diseases")(create_user_diseases)

bp_user.patch("/diseases/<disease_id>")(update_diseases)

bp_user.delete("/diseases/<disease_id>")(delete_user_diseases)
