"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field

from entregaAlpes.modulos.envios.dominio import objetos_valor as ov
from entregaAlpes.modulos.envios.dominio.eventos import EnvioCancelado, EnvioCourierConfirmada, EnvioCourierDefinido, EnvioCreado, EnvioReProgramado
from entregaAlpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Envio(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    id_pedido: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoEnvio = field(default=ov.EstadoEnvio.PENDIENTE)
    courier: ov.Courier = field(default=None)
    destino: ov.Destino = field(default=None)
    facilitaciones: list[ov.Facilitacion] = field(default_factory=list[ov.Facilitacion])

    def crear_envio(self):
        self.estado = ov.EstadoEnvio.PENDIENTE

        self.agregar_evento(EnvioCreado(id=self.id, id_pedido=self.id_pedido,
         facilitaciones=self.facilitaciones, destino=self.destino))

    def reprogramar_envio(self):
        self.estado = ov.EstadoEnvio.REPROGRAMADO

        self.agregar_evento(EnvioReProgramado(self.id_pedido, self.fecha_actualizacion))

    def cancelar_envio(self):
        self.estado = ov.EstadoEnvio.CANCELADO

        self.agregar_evento(EnvioCancelado(self.id_pedido, self.fecha_actualizacion))
    
    def definir_courier(self):
        self.estado = ov.EstadoEnvio.ENVIO_EDA

        self.agregar_evento(EnvioCourierDefinido(self.id_pedido, self.fecha_actualizacion))

    def confirmar_courier(self):
        self.estado = ov.EstadoEnvio.ENVIO_TERCERO

        self.agregar_evento(EnvioCourierConfirmada(self.id_pedido, self.fecha_actualizacion))