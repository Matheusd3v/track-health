from app.models.doctor_model import DoctorModel
from sqlalchemy.exc import DataError

def get_invalid_data_type(data):

    valid_types ={ 
        "date": str,
        "description": str,
        "doctor_id":str
    }

    invalid_data = []

    for key,value in data.items():
        if valid_types.get(key) != type(value):
            invalid_data.append(key)
    return invalid_data

def check_appointment_id(appointment, user): 

    appointment_id = str(appointment.user_id)
    user_id = user["id"]
    return  appointment_id == user_id

def check_data_keys(data):
    valid_keys = ['date', 'description','doctor_id']
    return all(key in valid_keys for key in data)

def check_not_nullable_keys(data):
    not_nullable_keys = ['date','doctor_id']
    return all(key in data for key in not_nullable_keys)

def check_doctor(doctor_id):
    try:
        doctor = DoctorModel.query.filter_by(id = doctor_id).first()
    except DataError:
        doctor = None
    return doctor