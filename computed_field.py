from pydantic import BaseModel, EmailStr , computed_field
from typing import List, Optional

class ContactInfo(BaseModel):
    email: EmailStr
    phone: str

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height:float
    married: Optional[bool] = None
    allergies: List[str]
    contact_deatils: ContactInfo

    @computed_field()
    @property
    def bmi(self) -> float:
        bmi = self.weight / ((self.height/100) ** 2)
        return round(bmi, 2)
   


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print("bmi" , patient.bmi)
    print(patient.allergies)
    print(patient.contact_deatils)
    print("Data inserted successfully")

patient_info = { "name": "John Doe", "age": '20' , "weight": 70.5, "height":1.5 ,"allergies": ["pollen", "nuts"], "contact_deatils": {"email": "jhon@hdfc.com" , "phone":"9083729202"} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)