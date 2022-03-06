from typing import Dict


def check_data_keys(data):
    valid_keys = ['street', 'number', 'district','city','complement','address_id']
    return all(key in valid_keys for key in data)

def get_invalid_data(data):

    valid_types ={ 
        'address_id':str,
        'street': str,
        "number": int,
        "district": str,
        "city": str,
        "complement":str
    }

    invalid_data = []

    for key,value in data.items():
        if not isinstance(value, valid_types[key]):
            invalid_data.append(key)
    return invalid_data

def remove_spaces(value: str) -> str:
    value_list = value.split()
    value_list[0] = value_list[0].capitalize()
    new_value = " ".join(value_list)
    
    return new_value

def address_normalize(data: Dict):
    if data.get('street'):
        data['street'] = remove_spaces(data['street']).title()
    if data.get('district'):
        data['district'] = remove_spaces(data['district']).title()
    if data.get('city'):
        data['city'] = remove_spaces(data['city']).title()
    if data.get('complement'):
        data['complement'] = remove_spaces(data['complement'])


