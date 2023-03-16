from entregaAlpes.seedwork.aplicacion.comandos import Comando, ComandoHandler
from entregaAlpes.modulos.envios.aplicacion.dto import CourierDTO
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from dataclasses import dataclass, field
from .base import EnvioBaseHandler


@dataclass
class RevertirAsignacionCourier(Comando):
    id: str
    courier: CourierDTO
    id_pedido: str


class RevertirAsignacionCourierHandler(EnvioBaseHandler):
    def handle(self, comando: RevertirAsignacionCourier):
        print("################ REVIRTIENDO ASIGNACION DE COURIER ###############")
        print(comando)
        #UnidadTrabajoPuerto.rollback()
        # TODO: Enviar evento para reprogramar el envio


@comando.register(RevertirAsignacionCourier)
def ejecutar_comando_crear_reserva(comando: RevertirAsignacionCourier):
    handler = RevertirAsignacionCourierHandler()
    handler.handle(comando)