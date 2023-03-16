import strawberry
import typing

from strawberry.types import Info
from bff_soli import utils
from bff_soli.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_solicitud(self, id_usuario: str, id_correlacion: str, info: Info) -> SolicitudRespuesta:
        print(f"ID Usuario: {id_usuario}, ID Correlación: {id_correlacion}")
        payload = dict(
            id_usuario = id_usuario,
            id_correlacion = id_correlacion,
            fecha_creacion = utils.time_millis()
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoSolicitud",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-solicitud", "public/default/comando-crear-solicitud")
        
        return SolicitudRespuesta(mensaje="Procesando Mensaje", codigo=203)