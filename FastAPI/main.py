from fastapi import FastAPI
from users import users_list
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return "hola estoy en main"

@app.get("/usersjson")
async def json():
    return [{"name":"Nicolas", "surname":"Urbaez", "age":33, "email":"aran.nick15@gmail.com"}][0]


@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)

# Query  ?id=1
@app.get("/userquery/")
async def userquery(id:int):
    return search_user(id)
    
def search_user(id:int):
    userquery = filter(lambda user: user.id == id, users_list)
    try:
        return list(userquery)[0]
    except:
        return {"Error":"Usuario no encontrado"}
    