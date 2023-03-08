from pulsar.schema import *
from entregaAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from entregaAlpes.seedwork.infraestructura.utils import time_millis
import uuid

class SolicitudCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoReservaCreada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = SolicitudCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)