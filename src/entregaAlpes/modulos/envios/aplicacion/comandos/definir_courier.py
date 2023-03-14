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
class DefinirCourier(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    facilitaciones: list[FacilitacionDTO]
    destino: DestinoDTO


class DefinirCourierHandler(EnvioBaseHandler):
    
    def handle(self, comando: DefinirCourier):
        print("######### MANEJANDO COMANDO DefinirCourier ###############")
        
        envio_dto = EnvioDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   facilitaciones=comando.facilitaciones
            ,   destino=comando.destino)
        print(envio_dto)
        envio: Envio = self.fabrica_envios.crear_objeto(envio_dto, MapeadorEnvio())
        envio.definir_courier()

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioEnvio)
        print(envio)
        # UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, envio)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()
        # evento = EnvioCreado(envio_dto.id, envio_dto.fecha_creacion, envio_dto.id_pedido,
        # envio_dto.fecha_actualizacion, envio_dto.fecha_creacion, envio_dto.facilitaciones, envio_dto.destino)
        # dispatcher.send(signal=f'{type(evento).__name__}Dominio', mensaje=evento)


@comando.register(DefinirCourier)
def ejecutar_comando_definir_courier(comando: DefinirCourier):
    handler = DefinirCourierHandler()
    handler.handle(comando)
    