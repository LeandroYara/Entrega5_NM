""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de envios

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de envios

"""

from entregaAlpes.config.db import db
from entregaAlpes.modulos.envios.dominio.repositorios import RepositorioEnvio, RepositorioLogisticaEnvio, RepositorioEventosEnvios
from entregaAlpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Producto, Facilitacion
from entregaAlpes.modulos.envios.dominio.entidades import Envio, LogisticaEnvio
from entregaAlpes.modulos.envios.dominio.fabricas import FabricaEnvios
from .dto import Envio as EnvioDTO, LogisticaEnvio as LogisticaEnvioDTO, EventosEnvio as EventosEnvioDTO
from .mapeadores import MapeadorEnvio, MapeadorLogisticaEnvio, MapadeadorEventosEnvio
from uuid import UUID
import logging
from pulsar.schema import *

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class RepositorioEnvioSQLite(RepositorioEnvio):

    def __init__(self):
        self._fabrica_envios: FabricaEnvios = FabricaEnvios()

    @property
    def fabrica_envios(self):
        return self._fabrica_envios

    def _obtener_por_id(self, id: UUID) -> EnvioDTO:
        return db.session.query(EnvioDTO).filter_by(id=str(id)).one()

    def _obtener_por_id_pedido(self, id_pedido: UUID) -> EnvioDTO:
        return db.session.query(EnvioDTO).filter_by(id_pedido=str(id_pedido)).one()

    def obtener_por_id(self, id: UUID) -> Envio:
        envio_dto = self._obtener_por_id(id=id)
        return self.fabrica_envios.crear_objeto(envio_dto, MapeadorEnvio())
    
    def obtener_por_id_pedido(self, id_pedido: UUID) -> Envio:
        envio_dto = self._obtener_por_id_pedido(id_pedido=id_pedido)
        return self.fabrica_envios.crear_objeto(envio_dto, MapeadorEnvio())

    def obtener_todos(self) -> list[Envio]:
        # TODO
        raise NotImplementedError

    def agregar(self, envio: Envio):
        envio_dto: EnvioDTO = self.fabrica_envios.crear_objeto(envio, MapeadorEnvio())
        db.session.add(envio_dto)

    def actualizar(self, envio: Envio):
        # TODO
        raise NotImplementedError

    def eliminar(self, Envio_id: UUID):
        # TODO
        raise NotImplementedError



class RepositorioLogisticaEnvioSQLite(RepositorioLogisticaEnvio):

    def __init__(self):
        self._fabrica_envios: FabricaEnvios = FabricaEnvios()

    @property
    def fabrica_envios(self):
        return self._fabrica_envios

    def agregar(self, logistica_envio: LogisticaEnvio):
        envio_dto: LogisticaEnvioDTO = self.fabrica_envios.crear_objeto(logistica_envio, MapeadorLogisticaEnvio())
        db.session.add(envio_dto)
    
    def actualizar(self, logistica_envio: LogisticaEnvio):
        # TODO
        raise NotImplementedError

    def eliminar(self, logistica_envio_id: UUID):
        # TODO
        raise NotImplementedError
    
    def obtener_por_id(self, id: UUID) -> LogisticaEnvio:
        # TODO
        raise NotImplementedError
    
    def obtener_todos(self) -> list[LogisticaEnvio]:
        # TODO
        raise NotImplementedError


class RepositorioEventosEnviosSQLAlchemy(RepositorioEventosEnvios):

    def __init__(self):
        self._fabrica_envios: FabricaEnvios = FabricaEnvios()

    @property
    def fabrica_envios(self):
        return self._fabrica_envios

    def obtener_por_id(self, id: UUID) -> Envio:
        envio_dto = db.session.query(EnvioDTO).filter_by(id=str(id)).one()
        return self.fabrica_envios.crear_objeto(envio_dto, MapadeadorEventosEnvio())

    def obtener_todos(self) -> list[Envio]:
        raise NotImplementedError

    def agregar(self, evento):
        envio_evento = self.fabrica_envios.crear_objeto(evento, MapadeadorEventosEnvio())

        parser_payload = JsonSchema(envio_evento.data.__class__)
        json_str = parser_payload.encode(envio_evento.data)

        evento_dto = EventosEnvioDTO()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_pedido)
        evento_dto.fecha_evento = evento.fecha_evento
        evento_dto.version = str(envio_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(envio_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, envio: Envio):
        raise NotImplementedError

    def eliminar(self, envio_id: UUID):
        raise NotImplementedError
