from fastapi import FastAPI
from users import users_list, User
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

@app.post("/user")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error":"El Usuario ya existe"}
    else:
        users_list.append(user)
        return {"Usuario Creado":"Exitosamente"}


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
    

    
    