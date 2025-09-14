from pydantic import BaseModel
from typing import List , Dict


class Patient(BaseModel):
    name:str    
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_deatils:Dict[str,str]    

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_deatils)
    print("Data inserted successfully")

patient_info = { "name": "John Doe", "age": '20' , "weight": 70.5, "married": False, "allergies": ["pollen", "nuts"], "contact_deatils": {"email": "jhon@gmail.com"} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)