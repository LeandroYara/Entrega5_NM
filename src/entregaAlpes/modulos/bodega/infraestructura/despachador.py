import pulsar
from pulsar.schema import *

from entregaAlpes.modulos.bodega.infraestructura.shema.v1.eventos import EventoOrdenCreada, OrdenCreadaPayload
from entregaAlpes.modulos.bodega.infraestructura.shema.v1.comandos import ComandoCrearOrden, ComandoCrearOrdenPayload
from entregaAlpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoOrdenCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = OrdenCreadaPayload(
                id_reserva = str(evento.id_reserva),
                estado = str(evento.estado),
                fecha_creacion = int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoOrdenCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoOrdenCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearOrdenPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearOrden(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearOrden))