from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.bodega.infraestructura.repositorios import RepositorioOrdenes
from dataclasses import dataclass
from .base import OrdenQueryBaseHandler
from aeroalpes.modulos.bodega.aplicación.mapeadores import MapeadorOrden
import uuid

@dataclass
class ObtenerOrden(Query):
    id: str

class ObtenerOrdenHandler(OrdenQueryBaseHandler):

    def handle(self, query: ObtenerOrden) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        orden =  self.fabrica_bodega.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorOrden())
        return QueryResultado(resultado=orden)

@query.register(ObtenerOrden)
def ejecutar_query_obtener_Orden(query: ObtenerOrden):
    handler = ObtenerOrdenHandler()
    return handler.handle(query)