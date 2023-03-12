from entregaAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from entregaAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from entregaAlpes.modulos.bodega.dominio.entidades import Orden
from .dto import OrdenDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO()

        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__
class MapeadorOrden(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Orden.__class__

    def locacion_a_dict(self, locacion):
        if not locacion:
            return dict(codigo=None, nombre=None, fecha_actualizacion=None, fecha_creacion=None)
        
        return dict(
                    codigo=locacion.codigo
                ,   nombre=locacion.nombre
                ,   fecha_actualizacion=locacion.fecha_actualizacion.strftime(self._FORMATO_FECHA)
                ,   fecha_creacion=locacion.fecha_creacion.strftime(self._FORMATO_FECHA)
        )
        

    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        #Esto toca actualizarlo con las listas de objetos
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        estado =entidad.estado
        #itinerarios = list()
        return OrdenDTO(fecha_creacion, fecha_actualizacion, _id, estado)

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        Orden = Orden()
        
        return Orden



