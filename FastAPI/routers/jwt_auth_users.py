from pydantic import BaseModel
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta



ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

router = APIRouter(prefix="/jwt", tags=["jwt"])

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt= CryptContext(schemes=["bcrypt"])


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
        "password":"$2a$12$nhowIY02eOmTxTL/5E7DcO/Mdq6jlcq39gpVLRFhZVOeUIxJl4AAa",
        "name":"Nicolas",
        "surname":"Urbaez",
        "age":33,
        "email":"aran.nick15@gmail.com",
        "disable":False
    },
    "nicolas2" :{
        "id": 0,
        "username":"nikoi19",
        "password":"$2a$12$YNqWeQs9mc/qoP8iSKodfOlj3ml9c8fSisghmUVgklVCoaYVbW8bC",
        "name":"Nicolas",
        "surname":"Urbaez",
        "age":33,
        "email":"aran.nick15@gmail.com",
        "disable":True
    }
}
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):    
    user_db = users_db.get(form.username)    
    if not user_db:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El  usuario no es correcto")    
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario Inactivo")    
    
    expire = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_DURATION)

   # access_token= {"sub":user.username, ""}


        
    return {"access_token" : user.username,"token_type " : "bearer"}








def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticación inválidas", 
            headers={"WWW-Authenticate" : "Bearer"})
    
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario Inactivo")
    
    return user



@router.get("/me")
async def me(user: User = Depends(current_user)):
     return user

