from fastapi import APIRouter
from app.schemas.equipo import EquipoCreate, EquipoResponse
from app.services import equipo_service

router = APIRouter(prefix="/equipos", tags=["Equipos"])

@router.get("/", response_model=list[EquipoResponse])
def get_equipos():
    return equipo_service.obtener_equipos()

@router.get("/{equipo_id}", response_model=EquipoResponse)
def get_equipo(equipo_id: int):
    return equipo_service.obtener_equipo(equipo_id)

@router.post("/", response_model=EquipoResponse)
def post_equipo(datos: EquipoCreate):
    return equipo_service.crear_equipo(datos)

@router.put("/{equipo_id}", response_model=EquipoResponse)
def put_equipo(equipo_id: int, datos: EquipoCreate):
    return equipo_service.actualizar_equipo(equipo_id, datos)

@router.delete("/{equipo_id}", response_model=EquipoResponse)
def delete_equipo(equipo_id: int):
    return equipo_service.eliminar_equipo(equipo_id)
