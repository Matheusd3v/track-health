from flask import Blueprint
from app.controllers.exams_controller import create_user_exam, delete_user_exam, get_user_exams, update_exam
from app.controllers.surgery_controller import create_surgery_user, delete_user_surgery, update_user_surgery
from app.controllers.user_controller import create_user, delete_user, get_user, login, update_user
from app.controllers.user_drug_controller import create_drug_data, delete_drug_data, get_user_drug, update_user_drug_data

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

bp_user.post("surgery")(create_surgery_user)

bp_user.patch("surgery/<id>")(update_user_surgery)

bp_user.delete("surgery/<id>")(delete_user_surgery)

bp_user.get("/drug")(get_user_drug)

bp_user.post("/drug")(create_drug_data)

bp_user.patch("/drug/<drug_id>")(update_user_drug_data)

bp_user.delete("/drug/<drug_id>")(delete_drug_data)