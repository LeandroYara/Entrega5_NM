from abc import ABC
from entregaAlpes.seedwork.dominio.repositorios import Repositorio

class RepositorioOrdenes(Repositorio, ABC):
    ...

class RepositorioBodegas(Repositorio, ABC):
    ...
