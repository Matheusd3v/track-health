def get_invalid_data(data):

    valid_types ={ 
        'name': str,
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
    valid_keys = ['name', 'date', 'description','doctor_id']
    return all(key in valid_keys for key in data)

def check_not_nullable_keys(data):
    not_nullable_keys = ['name','date']
    return all(key in data for key in not_nullable_keys)

def check_date_type(date):
    month = date.split("/")[0]
    return int(month) < 12