from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.envios.aplicacion.dto import EnvioDTO, FacilitacionDTO, CourierDTO, DestinoDTO
from .base import EnvioBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.envios.dominio.entidades import Envio
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.envios.aplicacion.mapeadores import MapeadorReserva
from aeroalpes.modulos.envios.infraestructura.repositorios import RepositorioReservas

@dataclass
class EnviarPorEda(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    facilitaciones: list[FacilitacionDTO]
    courier: CourierDTO
    destino: DestinoDTO


class EnviarPorEdaHandler(EnvioBaseHandler):
    
    def handle(self, comando: EnviarPorEda):
        reserva_dto = EnvioDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   facilitaciones=comando.facilitaciones
            ,   courier=comando.courier
            ,   destino=comando.destino)

        envio: Envio = self.fabrica_envios.crear_objeto(reserva_dto, MapeadorReserva())
        envio.crear_reserva(envio)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, envio)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(EnviarPorEda)
def ejecutar_comando_crear_reserva(comando: EnviarPorEda):
    handler = CrearReservaHandler()
    handler.handle(comando)
    