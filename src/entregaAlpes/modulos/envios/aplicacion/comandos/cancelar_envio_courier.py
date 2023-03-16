from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.modulos.envios.aplicacion.dto import CourierDTO
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from dataclasses import dataclass, field
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregaAlpes.modulos.envios.infraestructura.repositorios import RepositorioLogisticaEnvio
from pydispatch import dispatcher
from entregaAlpes.modulos.envios.dominio.eventos import AsignacionDeCourierFallida
from .base import EnvioBaseHandler


@dataclass
class CancelarEnvioCourier(Comando):
    id: str
    courier: CourierDTO
    id_pedido: str


class CancelarEnvioCourierHandler(EnvioBaseHandler):
    def handle(self, comando: CancelarEnvioCourier):
        print(comando)
        #repositorio = self.fabrica_repositorio.crear_objeto(RepositorioLogisticaEnvio)
        #logistica_envio.definir_courier()

        #UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, comando.id_pedido)
        #UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.rollback()

        evento = AsignacionDeCourierFallida(
            courier=comando.courier,
            id_pedido=comando.id_pedido,
        )
        dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)


@comando.register(CancelarEnvioCourier)
def ejecutar_comando_crear_reserva(comando: CancelarEnvioCourier):
    handler = CancelarEnvioCourierHandler()
    handler.handle(comando)
