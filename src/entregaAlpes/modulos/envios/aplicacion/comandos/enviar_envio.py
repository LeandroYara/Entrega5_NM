from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO, FacilitacionDTO, CourierDTO, DestinoDTO
from .base import EnvioBaseHandler
from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from entregaAlpes.modulos.envios.dominio.entidades import Envio
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregaAlpes.modulos.envios.aplicacion.mapeadores import MapeadorEnvio
from entregaAlpes.modulos.envios.infraestructura.repositorios import RepositorioEnvio

@dataclass
class EnviarEnvio(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    facilitaciones: list[FacilitacionDTO]
    destino: DestinoDTO


class EnviarEnvioHandler(EnvioBaseHandler):
    
    def handle(self, comando: EnviarEnvio):
        ...
        # TODO: determinar courier y setearlo en el comando y re-enviarlo en pulsar
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, envio)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()


@comando.register(EnviarEnvio)
def ejecutar_comando_crear_reserva(comando: EnviarEnvio):
    handler = EnviarEnvioHandler()
    handler.handle(comando)
    