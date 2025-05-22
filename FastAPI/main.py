from fastapi import FastAPI
from routers import students, users, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(students.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
# http://127.0.0.1:8000/static/images/nico.jpg

@app.get("/")
async def main():
    return {"Este es el":"main"}

    
# Documentacion con Swagger: http://localhost:8000/docs
# Documentacion con Redocly: http://localhost:8000/redoc
    
