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
class ConfirmarCourier(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    facilitaciones: list[FacilitacionDTO]
    courier: CourierDTO
    destino: DestinoDTO


class ConfirmarCourierHandler(EnvioBaseHandler):
    
    def handle(self, comando: ConfirmarCourier):
        envio_dto = EnvioDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   facilitaciones=comando.facilitaciones
            ,   courier=comando.courier
            ,   destino=comando.destino)

        envio: Envio = self.fabrica_envios.crear_objeto(envio_dto, MapeadorEnvio())
        envio.crear_reserva(envio)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, envio)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(ConfirmarCourier)
def ejecutar_comando_crear_reserva(comando: ConfirmarCourier):
    handler = ConfirmarCourierHandler()
    handler.handle(comando)
    