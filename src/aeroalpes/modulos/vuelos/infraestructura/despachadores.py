import pulsar
from pulsar.schema import *

from aeroalpes.modulos.vuelos.infraestructura.schema.v1.eventos import EventoReservaCreada, ReservaCreadaPayload
from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import  (
    ComandoCrearReserva, ComandoCrearReservaPayload, Itinerario, Odo, Segmento, Leg, Airport
)
from aeroalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ReservaCreadaPayload(
            id_reserva=str(evento.id_reserva), 
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoReservaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoReservaCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        it = [
            Itinerario(odos=[
                Odo(segmentos=[
                    Segmento(legs=[
                        Leg(
                            fecha_salida=leg.fecha_salida,
                            fecha_llegada=leg.fecha_llegada,
                            destino=Airport(
                                **leg.destino
                            ),
                            origen=Airport(
                                **leg.destino
                            ),
                        ) for leg in seg.legs
                    ]) for seg in odo.segmentos
                ]) for odo in ite.odos
            ]) for ite in comando.itinerarios
        ]
        payload = ComandoCrearReservaPayload(
            id_usuario=str(comando.id),
            # agregar itinerarios
            itinerarios=it
        )
        comando_integracion = ComandoCrearReserva(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearReserva))
