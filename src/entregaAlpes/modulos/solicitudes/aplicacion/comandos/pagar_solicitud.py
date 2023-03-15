from entregaAlpes.modulos.solicitudes.aplicacion.comandos.base import SolicitudBaseHandler
from entregaAlpes.modulos.solicitudes.aplicacion.dto import SolicitudDTO
from entregaAlpes.seedwork.aplicacion import comandos
from entregaAlpes.seedwork.aplicacion.comandos import Comando, ComandoHandler

class PagarSolicitud(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    monto: str
    id_cliente: str
    id_solicitud: str

class PagarSolicitudHandler(SolicitudBaseHandler):
    
    def handle(self, comando: PagarSolicitud):
        solicitud_dto = SolicitudDTO(id=comando.id
            ,   monto=comando.monto
            ,   id_cliente=comando.id_cliente
            ,   id_solicitud=comando.id_solicitud)
        
@comandos.register(PagarSolicitud)
def ejecutar_comando_pagar_solicitud(comando: PagarSolicitud):
    handler = PagarSolicitudHandler()
    handler.handle(comando)