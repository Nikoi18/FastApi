from pydantic import BaseModel
from fastapi import HTTPException, APIRouter

router = APIRouter(prefix="/user", tags=["user"])

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    email: str

users_list = [User(id=1,name="Nicolas",surname="Urbaez",age=33, email="aran.nick15@gmail.com"),
              User(id=2,name="Alberto",surname="Aranguren",age=33, email="aran.nick16@gmail.com")]

@router.get("/")
async def users():
    return users_list
# Path
@router.get("/{id}")
async def user(id:int):
    return search_user(id)

@router.post("/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail=f"El Usuario {user.name} con el ID: {user.id} ya existe.") 
    else:
        users_list.append(user)
        raise HTTPException(status_code=201, detail=f"El usuario {user.name} con el id: {user.id} ha siado agregado")        
    
@router.put("/")
async def user(user: User):

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            raise HTTPException(status_code=404, detail=f"Usuario {user.name} con el id: {user.id} actualizado")                   
    else:
        raise HTTPException(status_code=404, detail=f"Usuario {user.name} con el id: {user.id} no encontrado")        
     
@router.delete("/{id}")
async def user(id:int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            raise HTTPException(status_code=200, detail=f"Usuario {saved_user.name} con el ID: {saved_user.id} ha sido eliminado")            
    else:
        raise HTTPException(status_code=404, detail=f"Usuario con el id: {id} no encontrado")
    
def search_user(id:int):
    userquery = filter(lambda user: user.id == id, users_list)
    try:
        return list(userquery)[0]
    except:
        return {"Error":"Usuario no encontrado"}


