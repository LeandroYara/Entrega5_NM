from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class OrdenDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    estado: str = field(default_factory=str)