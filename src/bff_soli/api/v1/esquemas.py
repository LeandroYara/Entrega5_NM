import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


ENTREGAALPES_HOST = os.getenv("ENTREGAALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_solicitudes(root) -> typing.List["Solicitud"]:
    solicitudes_json = requests.get(f'http://{ENTREGAALPES_HOST}:5000/envios/solicitud').json()
    solicitudes = []

    for solicitud in solicitudes_json:
        solicitudes.append(
            Solicitud(
                fecha_creacion=datetime.strptime(solicitud.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(solicitud.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=solicitud.get('id'), 
                id_usuario=solicitud.get('id_usuario', '')
            )
        )

    return solicitudes

@strawberry.type
class Solicitud:
    id: str
    id_usuario: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime

@strawberry.type
class SolicitudRespuesta:
    mensaje: str
    codigo: int






