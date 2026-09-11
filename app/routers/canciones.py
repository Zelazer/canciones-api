from fastapi import APIRouter, status

from app.schemas.canciones import CancionCreate, CancionResponse
from app.services.cancionService import (
    listarCanciones,
    crearCancion,
    obtenerCancion,
    actualizarCancion,
    eliminarCancion
)

router = APIRouter(prefix="/canciones", tags=["Canciones"])


@router.get("/", response_model=list[CancionResponse], summary="Listar todas las canciones", description="Devuelve la lista completa de todas las canciones")
def getCanciones():
    return listarCanciones()

@router.get("/{cancionId}", response_model=CancionResponse, summary="Consultar una cancion por ID", description="Devuelve una cancion especifica. Responde 404 si el ID no existe")
def getCancion(cancionId: int):
    return obtenerCancion(cancionId)

@router.post("/", response_model=CancionResponse, status_code=status.HTTP_201_CREATED, summary="Crear una nueva cancion", description="Crea una cancion. Responde 400 si ya existe una cancion con ese nombre")
def postCancion(cancion: CancionCreate):
    return crearCancion(cancion)

@router.put("/{cancionId}", response_model=CancionResponse, summary="Actualizar una cancion", description="Actualiza los datos de una cancion. Responde 404 si el ID no existe. Responde 400 si el nuevo nombre ya esta utilizado")
def putCancion(cancionId: int, cancion: CancionCreate):
    return actualizarCancion(cancionId, cancion)

@router.delete("/{cancionId}", response_model=CancionResponse, summary="Eliminar una cancion", description="Elimina una cancion por ID. Responde 404 si el ID no existe")
def deleteCancion(cancionId: int):
    return eliminarCancion(cancionId)