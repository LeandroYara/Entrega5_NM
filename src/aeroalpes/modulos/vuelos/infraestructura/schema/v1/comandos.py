from pulsar.schema import *
from dataclasses import dataclass, field
from aeroalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class Airport(Record):
    codigo = String()
    nombre = String()

class Leg(Record):
    fecha_salida = String()
    fecha_llegada = String()
    origen = Airport()
    destino = Airport()

class Segmento(Record):
    legs = Array(Leg())

class Odo(Record):
    segmentos = Array(Segmento())

class Itinerario(Record):
    odos = Array(Odo())

class ComandoCrearReservaPayload(ComandoIntegracion):
    id_usuario = String()
    itinerarios = Array(Itinerario())

class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoCrearReservaPayload()