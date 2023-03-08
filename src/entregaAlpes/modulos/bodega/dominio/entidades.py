from datetime import datetime
from entregaAlpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field
import entregaAlpes.modulos.bodega.dominio.objetos_valor as ov
from .objetos_valor import Nombre, Capacidad, Ubicacion


@dataclass
class Bodega(Entidad):
    nombre: Nombre=field(default_factory=Nombre)
    capacidad: Capacidad=field(default_factory=Capacidad)
    ubicacion: Ubicacion=field(default_factory=Ubicacion)
    

