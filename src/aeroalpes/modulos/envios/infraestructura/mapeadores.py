""" Mapeadores para la capa de infrastructura del dominio de envios

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from aeroalpes.seedwork.dominio.repositorios import Mapeador
from aeroalpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Producto, Facilitacion, Courier, Destino
from aeroalpes.modulos.envios.dominio.entidades import Envio
from .dto import Envio as EnvioDTO
from .dto import Facilitacion as FacilitacionDTO

class MapeadorEnvio(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Envio.__class__

    def entidad_a_dto(self, entidad: Envio) -> EnvioDTO:
        
        envio_dto = EnvioDTO()
        envio_dto.fecha_creacion = entidad.fecha_creacion
        envio_dto.fecha_actualizacion = entidad.fecha_actualizacion
        envio_dto.id = str(entidad.id)
        envio_dto.courier_nombre = entidad.courier.nombre
        envio_dto.destino_nombre = entidad.destino.nombre
        envio_dto.destino_direccion = entidad.destino.direccion

        facilitacion_dtos = list()
        
        for facilitacion in entidad.facilitaciones:
            facilitacion_dtos.append(
                FacilitacionDTO(
                    producto_nombre=facilitacion.producto.nombre,
                    centro_distribucion = facilitacion.centro_distribucion.nombre,
                    centro_distribucion_direccion = facilitacion.centro_distribucion.direccion,
                    cantidad = facilitacion.cantidad,
                )
            )

        envio_dto.facilitaciones = facilitacion_dtos

        return envio_dto

    def dto_a_entidad(self, dto: EnvioDTO) -> Envio:
        envio = Envio(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        envio.courier = Courier(nombre=dto.courier_nombre)
        envio.destino = Destino(
            nombre=dto.destino_nombre,
            direccion=dto.destino_direccion,
        )
        envio.facilitaciones = list()

        facilitacion_dtos: list[Facilitacion] = [
            Facilitacion(
                centro_distribucion=CentroDistribucion(
                    nombre=facilitacion.centro_distribucion,
                    direccion=facilitacion.centro_distribucion_direccion,
                ),
                producto=Producto(
                    nombre=facilitacion.producto_nombre
                ),
                cantidad=facilitacion.cantidad,
            ) for facilitacion in dto.facilitaciones
        ]

        envio.facilitaciones = facilitacion_dtos
        return envio