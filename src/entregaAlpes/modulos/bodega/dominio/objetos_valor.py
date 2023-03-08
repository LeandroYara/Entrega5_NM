from entregaAlpes.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass
from entregaAlpes.seedwork.dominio.objetos_valor import Codigo, Locacion
from entregaAlpes.modulos.item.dominio.entidades import Item

@dataclass(frozen=True)
class Capacidad(ObjetoValor):
    capacidad: float

@dataclass(frozen=True)
class Ubicacion(ObjetoValor):
    latitud: float
    longitud: float
    nombre: str

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: str
        







