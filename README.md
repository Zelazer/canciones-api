# PARCIAL 1 - Juan David Herrera Gonzalez y Juan Camilo Diaz Herrera

# API de Canciones

## Nombre del proyecto
API de Canciones - API REST desarrollada con FastAPI

## Descripcion de la API
API que permite administrar un catalogo de canciones en memoria, aplicando la arquitectura por capas (routers, services, schemas). Permite listar, consultar, crear, actualizar y eliminar canciones, con validaciones de datos y reglas de negocio

## Recurso seleccionado
Canciones, con el siguiente modelo:

```json
{
  "id": 1,
  "nombre": "Bohemian Rhapsody",
  "artista": "Queen",
  "genero": "Rock",
  "album": "A Night at the Opera"
}
```

## Tecnologias utilizadas
- Python 3.11+
- FastAPI
- Pydantic v2
- Uvicorn (servidor ASGI)

## Estructura de carpetas
```
app/
├── main.py
├── routers/
│   └── canciones.py
├── services/
│   └── cancionService.py
└── schemas/
    └── canciones.py
requirements.txt
README.md
```

## Modelo del recurso

### CancionCreate
```
nombre: str = Field(..., min_length=3, max_length=30)
artista: str = Field(..., min_length=3, max_length=35)
genero: str = Field(..., min_length=3, max_length=20)
album: str = Field(default="Sin album", min_length=3, max_length=25)
```

### CancionResponse
```
id: int
nombre: str
artista: str
genero: str
album: str
```

## Endpoints disponibles
| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | /canciones/ | Listar todas |
| GET | /canciones/{cancionId} | Consultar una por ID |
| POST | /canciones/ | Crear |
| PUT | /canciones/{cancionId} | Actualizar |
| DELETE | /canciones/{cancionId} | Eliminar |

## Contratos de los endpoints

### Tabla general de contratos
| Metodo | Endpoint | Recibe | Devuelve exito | Posibles errores |
|--------|----------|--------|-----------------|-------------------|
| GET | /canciones/ | — | Lista de canciones 200 | — |
| GET | /canciones/{cancionId} | ID | Objeto 200 | 404 |
| POST | /canciones/ | JSON | Objeto creado 201 | 400, 422 |
| PUT | /canciones/{cancionId} | ID + JSON | Objeto actualizado 200 | 400, 404, 422 |
| DELETE | /canciones/{cancionId} | ID | Objeto eliminado 200 | 404 |

## Detalle de cada endpoint

### GET /canciones/

**Proposito:** devolver la lista completa de canciones registradas

**Datos de entrada:** ninguno

**Respuesta exitosa (200):**
```json
[
  {
    "id": 1,
    "nombre": "Bohemian Rhapsody",
    "artista": "Queen",
    "genero": "Rock",
    "album": "A Night at the Opera"
  }
]
```

**Errores posibles:** ninguno

### GET /canciones/{cancionId}

**Proposito:** consultar una cancion especifica por su ID

**Datos de entrada:** cancionId (int) en la ruta

**Respuesta exitosa (200):**
```json
{
  "id": 1,
  "nombre": "Bohemian Rhapsody",
  "artista": "Queen",
  "genero": "Rock",
  "album": "A Night at the Opera"
}
```

**Posibles errores:**
- 404 Not Found: no existe una cancion con ese ID

### POST /canciones/

**Proposito:** registrar una nueva cancion

**Datos de entrada:**
```json
{
  "nombre": "Bohemian Rhapsody",
  "artista": "Queen",
  "genero": "Rock",
  "album": "A Night at the Opera"
}
```

**Respuesta exitosa (201):**
```json
{
  "id": 1,
  "nombre": "Bohemian Rhapsody",
  "artista": "Queen",
  "genero": "Rock",
  "album": "A Night at the Opera"
}
```

**Posibles errores:**
- 400 Bad Request: ya existe una cancion con ese nombre
- 422 Unprocessable Entity: los datos no cumplen las validaciones

### PUT /canciones/{cancionId}

**Proposito:** actualizar los datos de una cancion existente

**Datos de entrada:** cancionId (int) en la ruta + JSON con los nuevos datos:
```json
{
  "nombre": "Bohemian Rhapsody (Remastered)",
  "artista": "Queen",
  "genero": "Rock",
  "album": "A Night at the Opera"
}
```

**Respuesta exitosa (200):**
```json
{
  "id": 1,
  "nombre": "Bohemian Rhapsody (Remastered)",
  "artista": "Queen",
  "genero": "Rock",
  "album": "A Night at the Opera"
}
```

**Posibles errores:**
- 404 Not Found: no existe una cancion con ese ID
- 400 Bad Request: el nuevo nombre ya esta en uso por otra cancion
- 422 Unprocessable Entity: los datos no cumplen las validaciones

### DELETE /canciones/{cancionId}

**Proposito:** eliminar una cancion por su ID

**Datos de entrada:** cancionId (int) en la ruta

**Respuesta exitosa (200):** devuelve el objeto eliminado
```json
{
  "id": 1,
  "nombre": "Bohemian Rhapsody",
  "artista": "Queen",
  "genero": "Rock",
  "album": "A Night at the Opera"
}
```

**Posibles errores:**
- 404 Not Found: no existe una cancion con ese ID

## Reglas de negocio implementadas
- No se permiten nombres de cancion duplicados, tanto al crear como al actualizar
- Todas las canciones deben cumplir las validaciones de longitud minima/maxima en nombre, artista, genero y album

## Instrucciones para instalar dependencias
```
python -m venv venv
source venv/bin/activate
En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Instrucciones para ejecutar la API
```
uvicorn app.main:app --reload
```

La API quedara disponible en http://127.0.0.1:8000

## Direccion de Swagger UI
http://127.0.0.1:8000/docs

Desde ahi se pueden probar todos los endpoints (GET, GET por ID, POST, PUT, DELETE) y verificar las validaciones y los errores 404/400
