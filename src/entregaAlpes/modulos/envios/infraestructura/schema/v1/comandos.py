from pulsar.schema import *
from dataclasses import dataclass, field
from entregaAlpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoEnviarPedidoPayload(ComandoIntegracion):
    id_usuario = String()
    courier_name = String()
    # TODO Cree los records para itinerarios

class ComandoEnviarPedido(ComandoIntegracion):
    data = ComandoEnviarPedidoPayload()