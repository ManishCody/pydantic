from pydantic import BaseModel, EmailStr , model_validator
from typing import List, Optional

class ContactInfo(BaseModel):
    email: EmailStr
    phone: Optional[str] = None 

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = None
    allergies: List[str]
    contact_deatils: ContactInfo

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age >=60 and not model.contact_deatils.phone:
            raise ValueError('Phone number is required for patients aged 60 or older')
        return model


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_deatils)
    print("Data inserted successfully")

patient_info = { "name": "John Doe", "age": '70' , "weight": 70.5, "allergies": ["pollen", "nuts"], "contact_deatils": {"email": "jhon@hdfc.com" } }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)