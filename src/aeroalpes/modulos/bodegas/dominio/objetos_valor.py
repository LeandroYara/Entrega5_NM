from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass
from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Ruta, Locacion

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool

@dataclass(frozen=True)
class Capacidad(ObjetoValor):
    capacidad: float





