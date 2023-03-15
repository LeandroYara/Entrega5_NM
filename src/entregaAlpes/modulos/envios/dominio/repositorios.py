""" Interfaces para los repositorios del dominio de vuelos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de vuelos

"""

from abc import ABC
from entregaAlpes.seedwork.dominio.repositorios import Repositorio

class RepositorioEnvio(Repositorio, ABC):
    ...

class RepositorioEventosEnvios(Repositorio, ABC):
    ...

# TODO: mover a logistica_envios
class RepositorioLogisticaEnvio(Repositorio, ABC):
    ...
