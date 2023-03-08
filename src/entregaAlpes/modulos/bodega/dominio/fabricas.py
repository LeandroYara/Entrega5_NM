from .entidades import Orden
from .reglas import DisponibilidadBodega, StockBodegaMayor0
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from entregaAlpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from entregaAlpes.seedwork.dominio.fabricas import Fabrica
from entregaAlpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            orden: Orden= mapeador.dto_a_entidad(obj)
            #Por ahora no hay validaciones dada la asincronia
            #self.validar_regla(DisponibilidadBodega(orden.itinerarios))
            #self.validar_regla(StockBodegaMayor0(Orden))
            
            return orden

@dataclass
class FabricaVuelos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_reserva = _FabricaOrden()
            return fabrica_reserva.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()