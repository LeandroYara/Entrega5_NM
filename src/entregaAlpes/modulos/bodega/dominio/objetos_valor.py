from entregaAlpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass
from entregaAlpes.seedwork.dominio.objetos_valor import Codigo, Locacion

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool

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
        







