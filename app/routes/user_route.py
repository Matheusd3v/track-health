from flask import Blueprint
from app.controllers.exams_controller import create_user_exam, delete_user_exam, get_user_exams, update_exam
from app.controllers.user_controller import create_user, delete_user, get_user, login, update_user
from app.controllers.allergies_controller import create_allergies, get_allergies, delete_allergy, update_allergy


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

bp_user.post("")(create_allergies)
bp_user.get("")(get_allergies)
bp_user.patch("/<allergy_id>")(update_allergy)
bp_user.delete("/<allergy_id>")(delete_allergy)
