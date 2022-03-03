from flask import Blueprint
from app.controllers.alcoholic_controller import create_alcoholic, delete_alcoholic, get_alcoholic, patch_alcoholic
from app.controllers.diseases_controller import create_user_diseases, update_diseases, delete_user_diseases, get_user_diseases
from app.controllers.exams_controller import create_user_exam, delete_user_exam, get_user_exams, update_exam
from app.controllers.medication_controller import create_medication_user, delete_medication_user, get_medications, update_medication_user
from app.controllers.surgery_controller import create_surgery_user, delete_user_surgery, update_user_surgery
from app.controllers.user_controller import create_user, delete_user, get_user, login, update_user
from app.controllers.user_drug_controller import create_drug_data, delete_drug_data, get_user_drug, update_user_drug_data
from app.controllers.user_physical_activity_controller import create_physical_activity, delete_physical_activity, get_physical_activity, patch_physical_activity
from app.controllers.smoker_controller import create_data, delete_data, get_data, patch_data


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


bp_user.post("/medication")(create_medication_user)
bp_user.get("/medication")(get_medications)
bp_user.patch("/medication/<medication_id>")(update_medication_user)
bp_user.delete("/medication/<medication_id>")(delete_medication_user)
bp_user.get("/diseases")(get_user_diseases)

bp_user.post("/diseases")(create_user_diseases)

bp_user.patch("/diseases/<disease_id>")(update_diseases)

bp_user.delete("/diseases/<disease_id>")(delete_user_diseases)

bp_user.post("surgery")(create_surgery_user)

bp_user.patch("surgery/<id>")(update_user_surgery)

bp_user.delete("surgery/<id>")(delete_user_surgery)

bp_user.post("/drug")(create_drug_data)

bp_user.get("/drug")(get_user_drug)

bp_user.patch("/drug/<drug_id>")(update_user_drug_data)

bp_user.delete("/drug/<drug_id>")(delete_drug_data)

bp_user.post("/physical_activity")(create_physical_activity)

bp_user.get("/physical_activity/<string:physical_activity_id>")(get_physical_activity)

bp_user.patch("/physical_activity/<string:physical_activity_id>")(patch_physical_activity)

bp_user.delete("/physical_activity/<string:physical_activity_id>")(delete_physical_activity)

bp_user.post("smoker")(create_data)

bp_user.get("/smoker/<string:smoker_id>")(get_data)

bp_user.patch("/smoker/<string:smoker_id>")(patch_data)

bp_user.delete("/smoker/<string:smoker_id>")(delete_data)

bp_user.post('/alcoholic')(create_alcoholic)

bp_user.get("/alcoholic/<string:alcoholic_id>")(get_alcoholic)

bp_user.patch("/alcoholic/<string:alcoholic_id>")(patch_alcoholic)

bp_user.delete("/alcoholic/<string:alcoholic_id>")(delete_alcoholic)

