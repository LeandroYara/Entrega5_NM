from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.envios.dominio.entidades import Envio
from aeroalpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Destino, Facilitacion
from .dto import EnvioDTO, FacilitacionDTO, ProductoDTO, CentroDistribucionDTO, DestinoDTO, CourierDTO

from datetime import datetime


class MapeadorEnvio(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Envio.__class__

    def entidad_a_dto(self, entidad: Envio) -> EnvioDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        facilitacion_dtos = list()
        
        for facilitacion in entidad.facilitaciones:
            facilitacion_dtos.append(
                FacilitacionDTO(
                    producto=ProductoDTO(nombre=facilitacion.producto.nombre),
                    centro_distribucion=CentroDistribucionDTO(
                        nombre=facilitacion.centro_distribucion.nombre,
                        direccion=facilitacion.centro_distribucion.direccion
                    ),
                    cantidad=facilitacion.cantidad,
                )
            )
        
        return EnvioDTO(
            fecha_creacion, fecha_actualizacion, _id, 
            DestinoDTO(nombre=entidad.destino.nombre, direccion=entidad.destino.direccion),
            facilitacion_dtos, CourierDTO(entidad.courier.nombre)
        )

    def dto_a_entidad(self, dto: EnvioDTO) -> Envio:
        envio = Envio()
        envio.facilitaciones = list()

        facilitaciones_dto: list[FacilitacionDTO] = dto.facilitaciones

        #for facilitacion in facilitaciones_dto:
            
        
        return envio



