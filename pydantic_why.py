from pydantic import BaseModel , EmailStr , Field
from typing import List  , Optional

class contactInfo(BaseModel):
    email:EmailStr
    phone:str

class Patient(BaseModel):
    name:str   = Field(min_length=3 , max_length=50) 
    age:int =  Field(ge=18, lt=100)
    weight:float
    married:Optional[bool] = None
    allergies:List[str]  # List is used for validating inner values also 
    contact_deatils: contactInfo   

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_deatils)
    print("Data inserted successfully")

patient_info = { "name": "John Doe", "age": '20' , "weight": 70.5, "allergies": ["pollen", "nuts"], "contact_deatils": {"email": "jhon@gmail.com" , "phone":"9083729202"} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)