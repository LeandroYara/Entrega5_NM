from entregaAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from entregaAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from entregaAlpes.modulos.envios.dominio.entidades import Envio
from entregaAlpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Destino, Facilitacion, Courier, Producto
from .dto import EnvioDTO, FacilitacionDTO, ProductoDTO, CentroDistribucionDTO, DestinoDTO, CourierDTO

from datetime import datetime

class  MapeadorEnvioDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> EnvioDTO:
        facilitaciones: list[FacilitacionDTO] = list()
        for facilitacion in externo.get('facilitaciones', list()):
            envio_dto.facilitaciones.append(FacilitacionDTO(
                producto=ProductoDTO(nombre=facilitacion.get('producto')),
                centro_distribucion=CentroDistribucionDTO(
                    nombre=facilitacion.get('centro_distribucion_nombre'),
                    direccion=facilitacion.get('centro_distribucion_direccion')
                ),
                cantidad=facilitacion.get("cantidad")
            ))
        
        envio_dto = EnvioDTO(
            destino = DestinoDTO(
            nombre=externo.get("destino").get("nombre"),
            direccion=externo.get("destino").get("direccion")),
            facilitaciones=facilitaciones,
        )

        return envio_dto

    def dto_a_externo(self, dto: EnvioDTO) -> dict:
        return dto.__dict__


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
        envio.courier = Courier(dto.courier.nombre)
        envio.destino = Destino(
            nombre=dto.destino.nombre,
            direccion=dto.destino.direccion,
        )

        facilitaciones: list[Facilitacion] = []

        for facilitacion in dto.facilitaciones:
            facilitaciones.append(Facilitacion(
                producto=Producto(facilitacion.producto.nombre),
                centro_distribucion=CentroDistribucion(
                    nombre=facilitacion.centro_distribucion.nombre,
                    direccion=facilitacion.centro_distribucion.direccion
                ),
                cantidad=facilitacion.cantidad
            ))
        
        envio.facilitaciones = facilitaciones
        return envio



