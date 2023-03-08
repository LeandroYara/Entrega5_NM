"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from entregaAlpes.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum


@dataclass(frozen=True)
class Courier(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class Producto(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class CentroDistribucion(ObjetoValor):
    nombre: str
    direccion: str

@dataclass(frozen=True)
class Destino(ObjetoValor):
    nombre: str
    direccion: str

@dataclass(frozen=True)
class Facilitacion(ObjetoValor):
    producto: Producto
    centro_distribucion: CentroDistribucion
    cantidad: int


class EstadoEnvio(str, Enum):
    PENDIENTE = "Pendiente"
    REPROGRAMADO = "Reprogramado"
    ENVIO_EDA = "Envio_Eda"
    ENVIO_TERCERO = "Envio_Tercero"
    CANCELADO = "Cancelado"