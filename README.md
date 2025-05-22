# API de Ejemplo con FastAPI

Este proyecto es una API desarrollada con FastAPI que implementa funcionalidades básicas de gestión de usuarios, autenticación y un endpoint de ejemplo para estudiantes.

## Características Principales

*   **Gestión de Usuarios**: Operaciones básicas para manejar una lista de usuarios (crear, leer, actualizar, eliminar).
*   **Autenticación**:
    *   **Autenticación Básica**: Implementación de un sistema de login simple.
    *   **Autenticación JWT**: Implementación de un sistema de login utilizando JSON Web Tokens para mayor seguridad, incluyendo hashing de contraseñas.
*   **Endpoint de Estudiantes**: Un endpoint simple para listar estudiantes.
*   **Validación de Datos**: Uso de Pydantic para la validación de modelos de datos.
*   **Estructura Modular**: El código está organizado en routers para una mejor mantenibilidad.

## Tecnologías Utilizadas

*   Python 3
*   FastAPI
*   Pydantic
*   JOSE (para la generación y manejo de JWT)
*   Passlib (para el hashing de contraseñas)
*   Uvicorn (como servidor ASGI)

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

*   `main.py`: (No proporcionado, pero asumido como el punto de entrada de la aplicación FastAPI donde se incluyen los routers).
*   `routers/`: Contiene los diferentes módulos de rutas de la API.
    *   `basic_auth_users.py`: Endpoints para autenticación básica.
    *   `jwt_auth_users.py`: Endpoints para autenticación con JWT.
    *   `users.py`: Endpoints para la gestión de usuarios.
    *   `students.py`: Endpoints para la gestión de estudiantes.

## Cómo Empezar (General)

1.  Clona el repositorio.
2.  Crea un entorno virtual e instala las dependencias (generalmente desde un archivo `requirements.txt` que deberías crear).
    ```bash
    pip install fastapi uvicorn pydantic python-jose passlib bcrypt
    ```
3.  Ejecuta la aplicación usando Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```
    (Asumiendo que tu instancia de FastAPI se llama `app` en un archivo `main.py`).
4.  Accede a la documentación interactiva de la API en `http://127.0.0.1:8000/docs`.

---

Este es mi primer README, espero que haya sido de utilidad, algo resumido y corto.

Gracias...
