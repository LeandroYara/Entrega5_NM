""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from entregaAlpes.seedwork.dominio.fabricas import Fabrica
from entregaAlpes.seedwork.dominio.repositorios import Repositorio
from entregaAlpes.seedwork.infraestructura.vistas import Vista
from entregaAlpes.modulos.solicitudes.infraestructura.vistas import VistaSolicitud
from entregaAlpes.modulos.solicitudes.dominio.entidades import Solicitud
from entregaAlpes.modulos.solicitudes.dominio.repositorios import RepositorioSolicitudes, RepositorioEventosSolicitudes
from .repositorios import RepositorioSolicitudesSQLAlchemy, RepositorioEventosSolicitudSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioSolicitudes:
            return RepositorioSolicitudesSQLAlchemy()
        elif obj == RepositorioEventosSolicitudes:
            return RepositorioEventosSolicitudSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')

@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Solicitud:
            return VistaSolicitud()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')