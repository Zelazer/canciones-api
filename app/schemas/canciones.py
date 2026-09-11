from pydantic import BaseModel, Field

class CancionCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30)
    artista: str = Field(..., min_length=3, max_length=35)
    genero: str = Field(..., min_length=3, max_length=20)
    album: str = Field(default="Sin album", min_length=3, max_length=25)

class CancionResponse(BaseModel):
    id: int
    nombre: str
    artista: str
    genero: str
    album: str
