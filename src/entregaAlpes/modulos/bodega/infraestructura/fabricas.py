from dataclasses import dataclass, field
from entregaAlpes.seedwork.dominio.fabricas import Fabrica
from entregaAlpes.seedwork.dominio.repositorios import Repositorio

from entregaAlpes.modulos.bodega.dominio.repositorios import RepositorioBodegas, RepositorioOrdenes
from .repositorios import RepositorioOrdenesSQLite, RepositorioBodegasSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaOrden(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioOrdenes.__class__:
            return RepositorioOrdenesSQLite()
        elif obj == RepositorioBodegas.__class__:
            return RepositorioBodegasSQLite()
        else:
            raise ExcepcionFabrica()
