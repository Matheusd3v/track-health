def check_data_keys(data):
    valid_keys = ['name', 'date', 'description','doctor_id']
    return all(key in valid_keys for key in data)

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

        return appointment['user_id'] == user['id']