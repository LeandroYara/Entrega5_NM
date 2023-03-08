"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field

from entregaAlpes.modulos.envios.dominio import objetos_valor as ov
from entregaAlpes.modulos.envios.dominio.eventos import EnvioCancelado, EnvioReProgramado, EnvioTercero, EnvioEda
from entregaAlpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Envio(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    id_pedido: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoEnvio = field(default=ov.EstadoEnvio.PENDIENTE)
    courier: ov.Courier
    destino: ov.Destino
    facilitaciones: list[ov.Facilitacion] = field(default_factory=list[ov.Facilitacion])

    def reprogramar_envio(self):
        self.estado = ov.EstadoEnvio.REPROGRAMADO

        self.agregar_evento(EnvioReProgramado(self.id, self.fecha_actualizacion))

    def cancelar_envio(self):
        self.estado = ov.EstadoEnvio.CANCELADO

        self.agregar_evento(EnvioCancelado(self.id, self.fecha_actualizacion))
    
    def enviar_por_eda(self):
        self.estado = ov.EstadoEnvio.ENVIO_EDA

        self.agregar_evento(EnvioEda(self.id, self.fecha_actualizacion))

    def enviar_por_tercero(self):
        self.estado = ov.EstadoEnvio.ENVIO_TERCERO

        self.agregar_evento(EnvioTercero(self.id, self.fecha_actualizacion))