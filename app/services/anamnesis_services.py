


def verify_fields_and_values(data: dict):
    required_fields = { 
        "diseases":"bool",
        "allergy":"bool",
        "continous_medication":"bool",
        "surgery":"bool",
        "alcoholic":"bool",
        "drug_user":"bool",
        "smoker":"bool",
        "physical_activity":"bool",
        "diabetes":"bool",
        "hipertension":"bool"
        }

    invalid_fields = []

    for key in data:
        if not required_fields.get(key) or type(data.get(key)) is not bool:

            invalid_fields.append(key)


    return invalid_fields, required_fields



def updating(data, anamnesis):
    valid_fields = [
            "diseases",
            "allergy",
            "continous_medication",
            "surgery",
            "alcoholic",
            "drug_user",
            "smoker",
            "physical_activity",
            "diabetes",
            "hipertension"
        ]

    for key,value in data.items():
        if key in valid_fields:
            setattr(anamnesis, key, value)