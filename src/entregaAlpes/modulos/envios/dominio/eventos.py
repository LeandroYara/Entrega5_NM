from __future__ import annotations
import uuid
from dataclasses import dataclass, field
from entregaAlpes.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO, FacilitacionDTO, CourierDTO, DestinoDTO


@dataclass
class EventoEnvio(EventoDominio):
    estado: str = None


@dataclass
class EnvioCreado(EventoEnvio):
    fecha_actualizacion: datetime = field(default=datetime.now())
    fecha_creacion: datetime = field(default=datetime.now())
    id: str
    facilitaciones: list[FacilitacionDTO] = None
    destino: DestinoDTO = None
    id_pedido: str = None


@dataclass
class EnvioReProgramado(EventoEnvio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioCancelado(EventoEnvio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioCourierDefinido(EventoEnvio):
    id_pedido: uuid.UUID = None
    facilitaciones: list[FacilitacionDTO] = None
    destino: DestinoDTO = None
    id_pedido: str = None
    courier: CourierDTO = None

@dataclass
class EnvioCourierConfirmada(EventoEnvio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None


# errors
@dataclass
class CreacionEnvioFallido(EventoEnvio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

# errors
@dataclass
class AsignacionDeCourierFallida(EventoEnvio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

# errors
@dataclass
class ConfirmacionDeCourierFallida(EventoEnvio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None