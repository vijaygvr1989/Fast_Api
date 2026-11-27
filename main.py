from fastapi import FastAPI
from pydantic import BaseModel

appl = FastAPI()

@appl.get("/")
def get_Func():
    return {"Message": "Hello World"}

@appl.get("/Update")
def get_new_tab():
    return {"Updated Get"}

@appl.get("/update/{name}")
def get_new_update(name:str):
    return {"Message": f"Hello {name}"}

class Student(BaseModel):
    name: str
    age : int
    roll: int

@appl.post("/Create_Post")
def create_Student(student : Student):
    return {
        "name" : student.name,
        "age" : student.age,
        "roll" : student.roll
    }