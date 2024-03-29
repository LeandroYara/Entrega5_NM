from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO, FacilitacionDTO, CourierDTO, DestinoDTO
from .base import EnvioBaseHandler
from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from entregaAlpes.modulos.envios.dominio.entidades import Envio
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregaAlpes.modulos.envios.aplicacion.mapeadores import MapeadorEnvio
from entregaAlpes.modulos.envios.infraestructura.repositorios import RepositorioEnvio
from pydispatch import dispatcher
from entregaAlpes.modulos.envios.dominio.eventos import ConfirmacionDeCourierFallida, EnvioCourierConfirmada


@dataclass
class ConfirmarCourier(Comando):
    id: str
    facilitaciones: list[FacilitacionDTO]
    courier: CourierDTO
    destino: DestinoDTO
    id_pedido: str


class ConfirmarCourierHandler(EnvioBaseHandler):
    
    def handle(self, comando: ConfirmarCourier):
        envio_dto = EnvioDTO(id=comando.id
            ,   id_pedido=comando.id_pedido
            ,   facilitaciones=comando.facilitaciones
            ,   courier=comando.courier
            ,   destino=comando.destino)

        #envio: Envio = self.fabrica_envios.crear_objeto(envio_dto, MapeadorEnvio())
        # envio.crear_reserva(envio)

        # repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

        # UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, envio)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()
        # Para triggear el final
        # evento = EnvioCourierConfirmada(
        #     courier=envio_dto.courier,
        #     id_pedido=envio_dto.id_pedido,
        # )
        # dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)

        # Para triggear compensaciones
        evento = ConfirmacionDeCourierFallida(
            courier=envio_dto.courier,
            id_pedido=envio_dto.id_pedido,
        )
        dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)


@comando.register(ConfirmarCourier)
def ejecutar_comando_crear_reserva(comando: ConfirmarCourier):
    handler = ConfirmarCourierHandler()
    handler.handle(comando)
    