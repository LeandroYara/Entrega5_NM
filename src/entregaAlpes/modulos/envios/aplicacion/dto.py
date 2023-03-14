from dataclasses import dataclass, field
from entregaAlpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CourierDTO(DTO):
    nombre: str

@dataclass(frozen=True)
class ProductoDTO(DTO):
    nombre: str

@dataclass(frozen=True)
class CentroDistribucionDTO(DTO):
    nombre: str
    direccion: str

@dataclass(frozen=True)
class DestinoDTO(DTO):
    nombre: str
    direccion: str

@dataclass(frozen=True)
class FacilitacionDTO(DTO):
    producto: ProductoDTO
    centro_distribucion: CentroDistribucionDTO
    cantidad: int

@dataclass(frozen=True)
class Courier(DTO):
    nombre: str


@dataclass(frozen=True)
class EnvioDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    facilitaciones: list[FacilitacionDTO] = field(default_factory=list)
    destino: DestinoDTO = field(default_factory=DestinoDTO)
    # esto se setea en uno de los pasos de la saga
    courier: CourierDTO = field(default=None)
    id_pedido: str = field(default_factory=str)


# @dataclass(frozen=True)
# class EnvioCourierDTO(DTO):
#     fecha_creacion: str = field(default_factory=str)
#     fecha_actualizacion: str = field(default_factory=str)
#     id: str = field(default_factory=str)
#     facilitaciones: list[FacilitacionDTO] = field(default_factory=list)
#     courier: CourierDTO = field(default_factory=CourierDTO)
#     destino: DestinoDTO = field(default_factory=DestinoDTO)