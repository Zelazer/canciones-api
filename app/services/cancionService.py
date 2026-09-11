from fastapi import HTTPException

from app.schemas.canciones import CancionCreate

_canciones: list[dict] = []
_next_id = 1

def listarCanciones() -> list[dict]:
    return _canciones

def obtenerCancion(cancionId: int) -> dict:
    for c in _canciones:
        if c["id"] == cancionId:
            return c
    raise HTTPException(
        status_code=404,
        detail="Cancion no encontrada"
    )

def crearCancion(cancion: CancionCreate) -> dict:
    global _next_id

    existe = False
    for c in _canciones:
        if c["nombre"].lower() == cancion.nombre.lower():
            existe = True

    if existe:
        raise HTTPException(status_code=400, detail="Ya existe una cancion con ese nombre")

    nuevaCancion = {
        "id": _next_id,
        "nombre": cancion.nombre,
        "artista": cancion.artista,
        "genero": cancion.genero,
        "album": cancion.album,
    }

    _canciones.append(nuevaCancion)
    _next_id += 1

    return nuevaCancion



def actualizarCancion(cancionId: int, cancionActualizada: CancionCreate) -> dict:
    cancion = obtenerCancion(cancionId)

    nombreDuplicado = False
    for c in _canciones:
        if c["nombre"].lower() == cancionActualizada.nombre.lower() and c["id"] != cancionId:
            nombreDuplicado = True

    if nombreDuplicado:
        raise HTTPException(status_code=400, detail="Ya existe una cancion con ese nombre")

    cancion["nombre"] = cancionActualizada.nombre
    cancion["artista"] = cancionActualizada.artista
    cancion["genero"] = cancionActualizada.genero
    cancion["album"] = cancionActualizada.album

    return cancion



def eliminarCancion(cancionId: int) -> dict:
    cancion = obtenerCancion(cancionId)

    _canciones.remove(cancion)

    return cancion