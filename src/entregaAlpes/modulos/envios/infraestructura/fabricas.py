""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from entregaAlpes.seedwork.dominio.fabricas import Fabrica
from entregaAlpes.seedwork.dominio.repositorios import Repositorio
from entregaAlpes.modulos.envios.dominio.repositorios import RepositorioEnvio
from .repositorios import RepositorioEnvioSQLite
from entregaAlpes.seedwork.dominio.excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioEnvio:
            return RepositorioEnvioSQLite()
        else:
            raise ExcepcionFabrica(f"No se puede crear la fabrica para {obj}")