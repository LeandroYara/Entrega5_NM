""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de bodega

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de bodega

"""

from entregaAlpes.config.db import db
from entregaAlpes.modulos.bodega.dominio.repositorios import RepositoriOrdenes, RepositorioProveedores
from entregaAlpes.modulos.bodega.dominio.entidades import Bodega, Orden
from entregaAlpes.modulos.bodega.dominio.fabricas import Fabricabodega
from .dto import orden as ordenDTO
from .mapeadores import Mapeadororden
from uuid import UUID

class RepositorioBodegasSQLite(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Orden:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Orden]:

        raise NotImplementedError

    def agregar(self, entity: Orden):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioOrdenesSQLite(RepositoriOrdenes):

    def __init__(self):
        self._fabrica_bodega: Fabricabodega = Fabricabodega()

    @property
    def fabrica_bodega(self):
        return self._fabrica_bodega

    def obtener_por_id(self, id: UUID) -> Orden:
        raise NotImplementedError

    def obtener_todos(self) -> list[Orden]:
        # TODO
        raise NotImplementedError

    def agregar(self, orden: Orden):
        raise NotImplementedError

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError