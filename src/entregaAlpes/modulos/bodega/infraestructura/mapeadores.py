""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from entregaAlpes.seedwork.dominio.repositorios import Mapeador

from entregaAlpes.modulos.bodega.dominio.entidades import Orden
from .dto import Reserva as ReservaDTO
from .dto import Itinerario as ItinerarioDTO

from .dto import Orden as OrdenDTO

class MapeadorReserva(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Orden.__class__

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