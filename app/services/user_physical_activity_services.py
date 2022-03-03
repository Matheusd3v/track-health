def check_data_keys(data):
    valid_keys = ['description', 'frequency']
    return all(key in valid_keys for key in data) 

def get_invalid_data(data):

    valid_types ={ 
        'description': str,
        "frequency": str,
    }

    invalid_data = []

    for key,value in data.items():
        if valid_types.get(key) != type(value):
            invalid_data.append(key)
    return invalid_data

def check_data_id(data, user): 

    data_id = str(data.user_id)
    user_id = user["id"]
    return  data_id == user_id