from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO, FacilitacionDTO, DestinoDTO
from .base import EnvioBaseHandler
from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from entregaAlpes.modulos.envios.dominio.entidades import Envio
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregaAlpes.modulos.envios.aplicacion.mapeadores import MapeadorEnvio
from entregaAlpes.modulos.envios.infraestructura.repositorios import RepositorioEnvio

@dataclass
class CrearEnvio(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    facilitaciones: list[FacilitacionDTO]
    destino: DestinoDTO
    id_pedido: str


class CrearEnvioHandler(EnvioBaseHandler):
    
    def handle(self, comando: CrearEnvio):
        print("###############CrearEnvioHandler###############")
        # TODO: determinar courier y setearlo en el comando y re-enviarlo en pulsar
        envio_dto = EnvioDTO(
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            id=comando.id,
            destino=comando.destino,
            facilitaciones=comando.facilitaciones,
            id_pedido=comando.id_pedido,
        )

        envio: Envio = self.fabrica_envios.crear_objeto(envio_dto, MapeadorEnvio())
        envio.crear_envio()

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioEnvio)
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, envio)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearEnvio)
def ejecutar_comando_crear_envio(comando: CrearEnvio):
    handler = CrearEnvioHandler()
    handler.handle(comando)
    