""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de envios

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de envios

"""

from entregaAlpes.config.db import db
from entregaAlpes.modulos.envios.dominio.repositorios import RepositorioEnvio, RepositorioLogisticaEnvio
from entregaAlpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Producto, Facilitacion
from entregaAlpes.modulos.envios.dominio.entidades import Envio, LogisticaEnvio
from entregaAlpes.modulos.envios.dominio.fabricas import FabricaEnvios
from .dto import Envio as EnvioDTO, LogisticaEnvio as LogisticaEnvioDTO
from .mapeadores import MapeadorEnvio, MapeadorLogisticaEnvio
from uuid import UUID
import logging
from sqlalchemy import update

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
