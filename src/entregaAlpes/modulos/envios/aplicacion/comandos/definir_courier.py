from entregaAlpes.seedwork.aplicacion.comandos import Comando
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO, FacilitacionDTO, CourierDTO, DestinoDTO
from .base import EnvioBaseHandler
from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from random import randint
from entregaAlpes.modulos.envios.dominio.entidades import Envio, LogisticaEnvio
from entregaAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregaAlpes.modulos.envios.aplicacion.mapeadores import MapeadorEnvio
from entregaAlpes.modulos.envios.infraestructura.repositorios import RepositorioLogisticaEnvio


couriers = [
    {"nombre": "FedEX", "is_externo": True},
    {"nombre": "UBER", "is_externo": True},
    {"nombre": "EDA", "is_externo": False},
    {"nombre": "UPS", "is_externo": True},
    {"nombre": "DHL", "is_externo": True},
]


@dataclass
class DefinirCourier(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    facilitaciones: list[FacilitacionDTO]
    destino: DestinoDTO
    id_pedido: str


class DefinirCourierHandler(EnvioBaseHandler):
    
    def handle(self, comando: DefinirCourier):
        print("######### MANEJANDO COMANDO DefinirCourier ###############")

        # TODO: Esto deberia estar en otro micro servicio donde se determine el Courier
        # tomando en consideracion datos como los productos facilitados
        courier_from_service = couriers[randint(0, len(couriers)-1)]
        courier = CourierDTO(**courier_from_service)

        logistica_envio = LogisticaEnvio(
            id_pedido=comando.id_pedido,
            courier=courier,
            id=comando.id
        )

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioLogisticaEnvio)
        logistica_envio.definir_courier()

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, logistica_envio)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(DefinirCourier)
def ejecutar_comando_definir_courier(comando: DefinirCourier):
    handler = DefinirCourierHandler()
    handler.handle(comando)
    