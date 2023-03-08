from tokenize import String
from pulsar.schema import *
from dataclasses import dataclass, field
from entregaAlpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearSolicitudPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearSolicitud(ComandoIntegracion):
    data = ComandoCrearSolicitudPayload()