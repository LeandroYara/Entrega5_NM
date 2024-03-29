import uuid
from pulsar.schema import *
from entregaAlpes.seedwork.infraestructura.utils import time_millis
from entregaAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class EnvioCreadoPayload(Record):
    id = String()
    id_pedido = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()


class EventoEnvioCreado(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EnvioCreadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EnvioCourierDefinidoPayload(Record):
    id = String()
    id_pedido = String()
    courier_name = String()
    courier_es_externo = Boolean()
    estado = String()
    fecha_creacion = Long()


class EventoEnvioCourierDefinido(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EnvioCourierDefinidoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConfirmacionDeCourierFallidaPayload(Record):
    id = String()
    id_pedido = String()
    courier_name = String()
    courier_es_externo = Boolean()
    estado = String()
    fecha_creacion = Long()


class EventoConfirmacionDeCourierFallida(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ConfirmacionDeCourierFallidaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AsignacionDeCourierFallidaPayload(Record):
    id = String()
    id_pedido = String()
    courier_name = String()
    courier_es_externo = Boolean()
    estado = String()
    fecha_creacion = Long()


class EventoAsignacionDeCourierFallida(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = AsignacionDeCourierFallidaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EnvioCourierConfirmadaPayload(Record):
    id = String()
    id_pedido = String()
    courier_name = String()
    courier_es_externo = Boolean()
    estado = String(default='CONFIRMADO')
    fecha_creacion = Long()


class EventoEnvioCourierConfirmada(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EnvioCourierConfirmadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)