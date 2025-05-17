from fastapi import APIRouter
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    email: str

router = APIRouter(prefix="/students", tags=["students"])

students_list=[Student(id=1,name="Nicolas",surname="Urbaez",age=33, email="aran.nick15@gmail.com"),
               Student(id=2,name="Alberto",surname="Urbaez",age=34, email="aran.nick15@gmail.com"),
               Student(id=3,name="Milagros",surname="Urbaez",age=30, email="aran.nick15@gmail.com")]

@router.get("/")
async def students():
    return students_list

@router.get("/{id}")
async def students(id: int):
    return students_list[id]



