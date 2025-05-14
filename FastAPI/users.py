from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    email: str



users_list = [User(id=1,name="Nicolas",surname="Urbaez",age=33, email="aran.nick15@gmail.com"),
              User(id=2,name="Alberto",surname="Aranguren",age=33, email="aran.nick16@gmail.com")]


