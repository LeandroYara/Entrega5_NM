""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Envio
from .reglas import MinimoUnProductoFacilitado, CantidadMinimaPorProductoFacilitado
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from aeroalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaEnvio(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            envio: Envio = mapeador.dto_a_entidad(obj)

            self.validar_regla(MinimoUnProductoFacilitado(envio.facilitaciones))
            self.validar_regla(CantidadMinimaPorProductoFacilitado(envio.facilitaciones))
            
            return envio

@dataclass
class FabricaEnvios(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Envio.__class__:
            fabrica_envio = _FabricaEnvio()
            return fabrica_envio.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()

