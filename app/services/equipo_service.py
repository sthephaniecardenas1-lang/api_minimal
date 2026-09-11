from fastapi import HTTPException

_equipos = [
    {"id": 1, "nombre": "Equipo A", "categoria": "Fútbol", "disponible": True},
    {"id": 2, "nombre": "Equipo B", "categoria": "Baloncesto", "disponible": True}
]

def obtener_equipos():
    return _equipos

def obtener_equipo(equipo_id: int):
    equipo = next((e for e in _equipos if e["id"] == equipo_id), None)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

def crear_equipo(datos):
    if any(e["nombre"].lower() == datos.nombre.lower() for e in _equipos):
        raise HTTPException(status_code=400, detail="El nombre del equipo ya está en uso")
    nuevo = {
        "id": len(_equipos) + 1,
        "nombre": datos.nombre,
        "categoria": datos.categoria,
        "disponible": True
    }
    _equipos.append(nuevo)
    return nuevo

def actualizar_equipo(equipo_id: int, datos) -> dict:
    equipo = next((e for e in _equipos if e["id"] == equipo_id), None)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    if any(e["nombre"].lower() == datos.nombre.lower() and e["id"] != equipo_id for e in _equipos):
        raise HTTPException(status_code=400, detail="El nombre del equipo ya está en uso")
    equipo["nombre"] = datos.nombre
    equipo["categoria"] = datos.categoria
    return equipo

def eliminar_equipo(equipo_id: int) -> dict:
    equipo = next((e for e in _equipos if e["id"] == equipo_id), None)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    _equipos.remove(equipo)
    return equipo
