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

def remove_spaces(value: str) -> str:
    value_list = value.split()
    value_list[0] = value_list[0].capitalize()
    new_value = " ".join(value_list)
    
    return new_value


def normalized_data(data: dict) -> dict:

    for key, value in data.items():    
        new_value = remove_spaces(value)
        data.update({key: new_value})

    return data        
