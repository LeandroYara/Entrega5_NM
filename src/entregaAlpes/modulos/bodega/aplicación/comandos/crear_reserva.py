
from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.modulos.bodega.aplicación.dto import ItinerarioDTO, OrdenDTO
from .base import CrearOrdenBaseHandler
from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from entregaAlpes.modulos.bodega.dominio.entidades import Orden
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from entregaAlpes.modulos.bodega.aplicación.mapeadores import MapeadorOrden
from entregaAlpes.modulos.bodega.infraestructura.repositorios import RepositorioOrden

@dataclass
class CrearOrden(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    estado: str


class CrearOrdenHandler(CrearOrdenBaseHandler):
    
    def handle(self, comando: CrearOrden):
        orden_dto = OrdenDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   estado=comando.estado)

        orden: Orden = self.fabrica_bodega.crear_objeto(orden_dto, MapeadorOrden())
        orden.crear_Orden(orden)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrden.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearOrden)
def ejecutar_comando_crear_Orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    