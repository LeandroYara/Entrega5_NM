""" Mapeadores para la capa de infrastructura del dominio de envios

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from entregaAlpes.seedwork.dominio.repositorios import Mapeador
from entregaAlpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Producto, Facilitacion, Courier, Destino
from entregaAlpes.modulos.envios.dominio.entidades import Envio, LogisticaEnvio
from .dto import Envio as EnvioDTO, LogisticaEnvio as LogisticaEnvioDTO
from .dto import Facilitacion as FacilitacionDTO

class MapeadorEnvio(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Envio.__class__

    def entidad_a_dto(self, entidad: Envio, envio_dto: EnvioDTO = None) -> EnvioDTO:
        
        envio_dto = EnvioDTO()
        envio_dto.fecha_creacion = entidad.fecha_creacion
        envio_dto.fecha_actualizacion = entidad.fecha_actualizacion
        envio_dto.id = str(entidad.id)
        if entidad.courier:
            # Esto puede ser None la primera vez ya que el Courier que enviara el Envio
            # se determina en un paso de la SAGA y tambien se actualizara este campo
            envio_dto.courier_nombre = entidad.courier.nombre
        envio_dto.destino_nombre = entidad.destino.nombre
        envio_dto.destino_direccion = entidad.destino.direccion
        envio_dto.id_pedido = entidad.id_pedido
        facilitacion_dtos = list()
        
        for facilitacion in entidad.facilitaciones:
            facilitacion_dtos.append(
                FacilitacionDTO(
                    producto_nombre=facilitacion.producto.nombre,
                    centro_distribucion = facilitacion.centro_distribucion.nombre,
                    centro_distribucion_direccion = facilitacion.centro_distribucion.direccion,
                    cantidad = facilitacion.cantidad,
                    id_pedido = envio_dto.id_pedido
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
        envio.id_pedido = dto.id_pedido

        envio.facilitaciones = facilitacion_dtos
        return envio
    

class MapeadorLogisticaEnvio(Mapeador):
    def obtener_tipo(self) -> type:
        return LogisticaEnvio.__class__
    
    def entidad_a_dto(self, entidad: LogisticaEnvio) -> LogisticaEnvioDTO:
        print("################# MapeadorLogisticaEnvio.entidad_a_dto ######################")
        logistica_envio_dto = LogisticaEnvioDTO()
        logistica_envio_dto.id = str(entidad.id)
        logistica_envio_dto.courier_nombre = entidad.courier.nombre
        logistica_envio_dto.is_externo = entidad.courier.is_externo
        logistica_envio_dto.id_pedido = entidad.id_pedido
        logistica_envio_dto.fecha_creacion = entidad.fecha_creacion
        logistica_envio_dto.fecha_actualizacion = entidad.fecha_actualizacion
        return logistica_envio_dto

    def dto_a_entidad(self, dto: LogisticaEnvioDTO) -> LogisticaEnvio:
        print("################# MapeadorLogisticaEnvio.dto_a_entidad ######################")