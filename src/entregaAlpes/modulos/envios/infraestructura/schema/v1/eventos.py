from pulsar.schema import *
from entregaAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class EnvioEdaPayload(Record):
    id_pedido = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoEnvioEda(EventoIntegracion):
    data = EnvioEdaPayload()


class EnvioTerceroPayload(Record):
    id_pedido = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoEnvioTercero(EventoIntegracion):
    data = EnvioEdaPayload()