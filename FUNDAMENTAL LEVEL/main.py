import asyncio
import json
from pathlib import Path
from typing import Optional
from uuid import uuid4

# Modelo de usuario
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Fundamentos del lenguaje + async/await para I/O
class Usuario(BaseModel):
    id: str | None = None
    name: dict
    age: int


# Endpoint GET con filtros por query string
@app.get("/api/v1/users")
async def users(
    id: Optional[str] = None,
    givenName: Optional[str] = None,
    familyName: Optional[str] = None,
    age: Optional[int] = None,
):
    """
    Obtiene usuarios filtrando por id, givenName, familyName y/o age usando query string.
    Ejemplo: /api/v1/users?givenName=Rupert&familyName=Muro
    """
    ruta = Path("usuarios.json")
    if not ruta.exists():
        raise HTTPException(
            status_code=404, detail="Archivo usuarios.json no encontrado"
        )
    try:
        contenido = await asyncio.to_thread(ruta.read_text, encoding="utf-8")
        usuarios = json.loads(contenido)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400, detail="Error de formato en el archivo JSON"
        )

    # Filtrado
    resultados = usuarios
    if id is not None:
        resultados = [u for u in resultados if u.get("id") == id]
    if givenName is not None:
        resultados = [
            u for u in resultados if u.get("name", {}).get("givenName") == givenName
        ]
    if familyName is not None:
        resultados = [
            u for u in resultados if u.get("name", {}).get("familyName") == familyName
        ]
    if age is not None:
        resultados = [u for u in resultados if u.get("age") == age]

    return resultados


# POST para agregar usuario
@app.post("/api/v1/users")
async def create_user(usuario: Usuario):
    ruta = Path("usuarios.json")
    if not ruta.exists():
        await asyncio.to_thread(ruta.write_text, "[]", encoding="utf-8")
    try:
        contenido = await asyncio.to_thread(ruta.read_text, encoding="utf-8")
        usuarios = json.loads(contenido)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400, detail="Error de formato en el archivo JSON"
        )
    # Generar id si no viene
    user_dict = usuario.dict()
    if not user_dict["id"]:
        user_dict["id"] = str(uuid4())
    # Validar id duplicado
    existe = any(u.get("id") == user_dict["id"] for u in usuarios)
    if existe:
        raise HTTPException(
            status_code=409, detail=f"El usuario con id {user_dict['id']} ya existe"
        )
    usuarios.append(user_dict)
    await asyncio.to_thread(
        ruta.write_text,
        json.dumps(usuarios, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return {"message": "Usuario agregado correctamente", "user": user_dict}
