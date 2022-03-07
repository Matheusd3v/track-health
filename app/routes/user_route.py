from flask import Blueprint
from app.controllers.alcoholic_controller import create_alcoholic, delete_alcoholic, get_alcoholic, patch_alcoholic
from app.controllers.anamnesis_controller import create_anamnesis, get_anamnesis, update_anamnesis
from app.controllers.diseases_controller import create_user_diseases, update_diseases, delete_user_diseases, get_user_diseases
from app.controllers.exam_files_controller import delete_exam_file, upload_exam_file
from app.controllers.exams_controller import create_user_exam, delete_user_exam, get_user_exams, update_exam
from app.controllers.medication_controller import create_medication_user, delete_medication_user, get_medications, update_medication_user
from app.controllers.surgery_controller import create_surgery_user, delete_user_surgery, get_user_surgerys, update_user_surgery
from app.controllers.user_controller import create_user, delete_user, get_user, login, update_user
from app.controllers.allergies_controller import create_allergies, get_allergies, delete_allergy, update_allergy
from app.controllers.user_drug_controller import create_drug_data, delete_drug_data, get_user_drug, update_user_drug_data
from app.controllers.profile_image_controller import delete_image_profile, get_image_profile, upload_image
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
bp_user.post("/exam/file/<exam_id>")(upload_exam_file)
bp_user.delete("/exam/file/<exam_id>")(delete_exam_file)

bp_user.post("/allergy")(create_allergies)
bp_user.get("/allergy")(get_allergies)
bp_user.patch("/allergy/<allergy_id>")(update_allergy)
bp_user.delete("/allergy/<allergy_id>")(delete_allergy)

bp_user.post("/medication")(create_medication_user)
bp_user.get("/medication")(get_medications)
bp_user.patch("/medication/<medication_id>")(update_medication_user)
bp_user.delete("/medication/<medication_id>")(delete_medication_user)

bp_user.get("/diseases")(get_user_diseases)
bp_user.post("/diseases")(create_user_diseases)
bp_user.patch("/diseases/<disease_id>")(update_diseases)
bp_user.delete("/diseases/<disease_id>")(delete_user_diseases)

bp_user.get("/surgery")(get_user_surgerys)
bp_user.post("surgery")(create_surgery_user)
bp_user.patch("surgery/<id>")(update_user_surgery)
bp_user.delete("surgery/<id>")(delete_user_surgery)

bp_user.post("/drug")(create_drug_data)
bp_user.get("/drug")(get_user_drug)
bp_user.patch("/drug")(update_user_drug_data)
bp_user.delete("/drug")(delete_drug_data)

bp_user.post("/physical_activity")(create_physical_activity)
bp_user.get("/physical_activity")(get_physical_activity)
bp_user.patch("/physical_activity")(patch_physical_activity)
bp_user.delete("/physical_activity")(delete_physical_activity)

bp_user.post("/smoker")(create_data)
bp_user.get("/smoker")(get_data)
bp_user.patch("/smoker")(patch_data)
bp_user.delete("/smoker")(delete_data)

bp_user.post('/alcoholic')(create_alcoholic)
bp_user.get("/alcoholic/<string:alcoholic_id>")(get_alcoholic)
bp_user.patch("/alcoholic/<string:alcoholic_id>")(patch_alcoholic)
bp_user.delete("/alcoholic/<string:alcoholic_id>")(delete_alcoholic)

bp_user.post("/anamnesis")(create_anamnesis)
bp_user.patch("/anamnesis")(update_anamnesis)
bp_user.get("/anamnesis")(get_anamnesis)

bp_user.post("/image-profile")(upload_image)
bp_user.get("/image-profile")(get_image_profile)
bp_user.delete("/image-profile")(delete_image_profile)

