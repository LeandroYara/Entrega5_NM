import pulsar
from pulsar.schema import *

from entregaAlpes.modulos.solicitudes.infraestructura.schema.v1.eventos import EventoReservaCreada, ReservaCreadaPayload
from entregaAlpes.modulos.solicitudes.infraestructura.schema.v1.comandos import ComandoCrearSolicitud, ComandoCrearSolicitudPayload
from entregaAlpes.seedwork.infraestructura import utils

from entregaAlpes.modulos.solicitudes.infraestructura.mapeadores import MapadeadorEventosSolicitud

class Despachador:
    def __init__(self):
        self.mapper = MapadeadorEventosSolicitud()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoReservaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearSolicitudPayload(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearSolicitud(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearSolicitud))
