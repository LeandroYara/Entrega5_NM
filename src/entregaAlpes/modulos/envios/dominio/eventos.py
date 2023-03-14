from __future__ import annotations
import uuid
from dataclasses import dataclass, field
from entregaAlpes.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
from entregaAlpes.modulos.envios.aplicacion.dto import EnvioDTO, FacilitacionDTO, CourierDTO, DestinoDTO


@dataclass
class EnvioCreado(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None
    fecha_creacion: datetime = None
    id: str
    facilitaciones: list[FacilitacionDTO] = None
    destino: DestinoDTO = None
    id_pedido: str = None


@dataclass
class EnvioReProgramado(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioCancelado(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioCourierDefinido(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioCourierConfirmada(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None