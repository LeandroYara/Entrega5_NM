""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de envios

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de envios

"""

from entregaAlpes.config.db import db
from entregaAlpes.modulos.envios.dominio.repositorios import RepositorioEnvio
from entregaAlpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Producto, Facilitacion
from entregaAlpes.modulos.envios.dominio.entidades import Envio
from entregaAlpes.modulos.envios.dominio.fabricas import FabricaEnvios
from .dto import Envio as EnvioDTO
from .mapeadores import MapeadorEnvio
from uuid import UUID
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class RepositorioEnvioSQLite(RepositorioEnvio):

    def __init__(self):
        self._fabrica_envios: FabricaEnvios = FabricaEnvios()

    @property
    def fabrica_envios(self):
        return self._fabrica_envios

    def obtener_por_id(self, id: UUID) -> Envio:
        envio_dto = db.session.query(EnvioDTO).filter_by(id=str(id)).one()
        return self.fabrica_envios.crear_objeto(envio_dto, MapeadorEnvio())

    def obtener_todos(self) -> list[Envio]:
        # TODO
        raise NotImplementedError

    def agregar(self, envio: Envio):
        envio_dto: EnvioDTO = self.fabrica_envios.crear_objeto(envio, MapeadorEnvio())
        db.session.add(envio_dto)

    def actualizar(self, Envio: Envio):
        # TODO
        raise NotImplementedError

    def eliminar(self, Envio_id: UUID):
        # TODO
        raise NotImplementedError