from datetime import datetime
from aeroalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field
import aeroalpes.modulos.bodegas.dominio.objetos_valor as ov
from .objetos_valor import Nombre, Email, Cedula, Rut


@dataclass
class Bodega(Entidad):
    id: Nombre = field(default_factory=Nombre)
    capacidad: Email = field(default_factory=Email)
