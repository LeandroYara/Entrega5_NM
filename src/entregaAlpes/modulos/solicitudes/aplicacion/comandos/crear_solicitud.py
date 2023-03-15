from entregaAlpes.modulos.solicitudes.infraestructura.mapeadores import MapeadorSolicitud
from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.modulos.solicitudes.aplicacion.dto import SolicitudDTO
from .base import CrearSolicitudBaseHandler
from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from entregaAlpes.modulos.solicitudes.dominio.entidades import Solicitud
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregaAlpes.modulos.solicitudes.aplicacion.mapeadores import MapeadorSo
from entregaAlpes.modulos.solicitudes.infraestructura.repositorios import RepositorioSolicitudes, RepositorioEventosSolicitudes

@dataclass
class CrearSolicitud(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    cliente: str


class CrearSolicitudHandler(CrearSolicitudBaseHandler):
    
    def handle(self, comando: CrearSolicitud): 
        solicitud_dto = SolicitudDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   cliente=comando.cliente)

        solicitud: Solicitud = self.fabrica_solicitudes.crear_objeto(solicitud_dto, MapeadorSolicitud())
        solicitud.crear_solicitud(solicitud)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSolicitudes)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosSolicitudes)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, solicitud, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.commit()


@comando.register(CrearSolicitud)
def ejecutar_comando_crear_reserva(comando: CrearSolicitud):
    handler = CrearSolicitudHandler()
    handler.handle(comando)
    