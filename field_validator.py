from pydantic import BaseModel, EmailStr , field_validator
from typing import List, Optional

class ContactInfo(BaseModel):
    email: EmailStr
    phone: str

    @field_validator('email')
    @classmethod
    def email_must_be_valid(cls, value):
        valid_domains = ['hdfc.com', 'icic.com']
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')
        return value

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = None
    allergies: List[str]
    contact_deatils: ContactInfo

    @field_validator('name')
    @classmethod
    def name_must_be_valid(cls, value):
        return value.upper()
    @field_validator('age', mode='after')
    @classmethod
    def age_must_be_valid(cls, value):
        if value < 18 or value > 100:
            raise ValueError('Age must be between 18 and 100')
        return value

   


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_deatils)
    print("Data inserted successfully")

patient_info = { "name": "John Doe", "age": '20' , "weight": 70.5, "allergies": ["pollen", "nuts"], "contact_deatils": {"email": "jhon@hdfc.com" , "phone":"9083729202"} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)