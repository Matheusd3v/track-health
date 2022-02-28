from flask import Blueprint
from app.controllers.exams_controller import create_user_exam
from app.controllers.user_controller import create_user, delete_user, get_user, login, update_user

bp_user = Blueprint("bp_user", __name__, url_prefix="/user")

bp_user.post("/register")(create_user)

bp_user.post("/login")(login)

bp_user.get("")(get_user)

bp_user.patch("")(update_user)

bp_user.delete("")(delete_user)

bp_user.post("/exam")(create_user_exam)