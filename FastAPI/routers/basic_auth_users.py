from pydantic import BaseModel
from fastapi import FastAPI

app= FastAPI()



class User(BaseModel):
    id: int
    username: str
    name: str
    surname: str
    age: int
    email: str
    disable: bool

class UserDB(User):
    password: str

users_db ={
    "nicolas": {
        "id": 0,
        "username":"nikoi18",
        "password":"123456",
        "name":"Nicolas",
        "surname":"Urbaez",
        "age":33,
        "email":"aran.nick15@gmail.com",
        "disable":False,},
    "nicolas2":{
        "id": 0,
        "username":"nikoi19",
        "password":"654321",
        "name":"Nicolas",
        "surname":"Urbaez",
        "age":33,
        "email":"aran.nick15@gmail.com",
        "disable":True,
                }}

def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])

