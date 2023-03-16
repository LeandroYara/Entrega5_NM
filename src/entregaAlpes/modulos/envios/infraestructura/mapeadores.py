""" Mapeadores para la capa de infrastructura del dominio de envios

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
from entregaAlpes.seedwork.infraestructura.utils import unix_time_millis
from entregaAlpes.seedwork.dominio.repositorios import Mapeador
from entregaAlpes.modulos.envios.dominio.objetos_valor import CentroDistribucion, Producto, Facilitacion, Courier, Destino
from entregaAlpes.modulos.envios.dominio.entidades import Envio, LogisticaEnvio
from entregaAlpes.modulos.envios.dominio.eventos import (
    EventoEnvio, EnvioCreado, EnvioCourierConfirmada, EnvioCourierDefinido,
    CreacionEnvioFallido, AsignacionDeCourierFallida, ConfirmacionDeCourierFallida
)
from .dto import Envio as EnvioDTO, LogisticaEnvio as LogisticaEnvioDTO
from .dto import Facilitacion as FacilitacionDTO
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

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


class MapadeadorEventosEnvio(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            EnvioCreado: self._entidad_a_envio_creado,
            EnvioCourierDefinido: self._entidad_a_envio_courier_definido,
            EnvioCourierConfirmada: self._entidad_a_envio_courier_confirmada,
            ConfirmacionDeCourierFallida: self._entidad_a_confirmacion_courier_fallida,
            AsignacionDeCourierFallida: self._entidad_a_asignacion_courier_fallida,
            CreacionEnvioFallido: self._entidad_a_creacion_envio_fallido,
        }

    def obtener_tipo(self) -> type:
        return EventoEnvio.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_envio_creado(self, entidad: EnvioCreado, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import EnvioCreadoPayload, EventoEnvioCreado

            payload = EnvioCreadoPayload(
                id_pedido=str(evento.id_pedido),
                #estado=str(evento.estado), 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoEnvioCreado(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'EnvioCreado'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'entregaAlpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_envio_courier_definido(self, entidad: EnvioCourierDefinido, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import EnvioCourierDefinidoPayload, EventoEnvioCourierDefinido

            payload = EnvioCourierDefinidoPayload(
                id_pedido=str(evento.id_pedido),
                courier_name=str(evento.courier.nombre),
                courier_es_externo=bool(evento.courier.is_externo),
                fecha_creacion=int(unix_time_millis(evento.fecha_evento))
            )
            evento_integracion = EventoEnvioCourierDefinido(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_evento))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'EnvioCourierDefinido'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'entregaAlpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)
    
    def _entidad_a_envio_courier_confirmada(self, entidad: EnvioCourierConfirmada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import EnvioCourierConfirmadaPayload, EventoEnvioCourierConfirmada

            payload = EnvioCourierConfirmadaPayload(
                id_pedido=str(evento.id_pedido),
                courier_name=str(evento.courier.nombre),
                courier_es_externo=bool(evento.courier.is_externo),
                fecha_creacion=int(unix_time_millis(evento.fecha_evento))
            )
            evento_integracion = EventoEnvioCourierConfirmada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_evento))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'EnvioCourierConfirmada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'entregaAlpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)
    
    def _entidad_a_confirmacion_courier_fallida(self, entidad: ConfirmacionDeCourierFallida, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import ConfirmacionDeCourierFallidaPayload, EventoConfirmacionDeCourierFallida

            payload = ConfirmacionDeCourierFallidaPayload(
                id_pedido=str(evento.id_pedido),
                courier_name=str(evento.courier.nombre),
                courier_es_externo=bool(evento.courier.is_externo),
                fecha_creacion=int(unix_time_millis(evento.fecha_evento))
            )
            evento_integracion = EventoConfirmacionDeCourierFallida(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_evento))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'ConfirmacionDeCourierFallida'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'entregaAlpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)
    
    def _entidad_a_asignacion_courier_fallida(self, entidad: AsignacionDeCourierFallida, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import EventoAsignacionDeCourierFallida, AsignacionDeCourierFallidaPayload

            payload = AsignacionDeCourierFallidaPayload(
                id_pedido=str(evento.id_pedido),
                courier_name=str(evento.courier.nombre),
                courier_es_externo=bool(evento.courier.is_externo),
                fecha_creacion=int(unix_time_millis(evento.fecha_evento))
            )
            evento_integracion = EventoAsignacionDeCourierFallida(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_evento))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'AsignacionDeCourierFallida'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'entregaAlpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)
    
    def _entidad_a_creacion_envio_fallido(self, entidad: CreacionEnvioFallido, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def entidad_a_dto(self, entidad: EventoEnvio, version=LATEST_VERSION) -> EnvioDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: EnvioDTO, version=LATEST_VERSION) -> Envio:
        print(dto)
        raise NotImplementedError