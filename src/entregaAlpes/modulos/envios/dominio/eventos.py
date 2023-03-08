from __future__ import annotations
from dataclasses import dataclass, field
from entregaAlpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
    
@dataclass
class EnvioReProgramado(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioCancelado(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioEda(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class EnvioTercero(EventoDominio):
    id_pedido: uuid.UUID = None
    fecha_actualizacion: datetime = None