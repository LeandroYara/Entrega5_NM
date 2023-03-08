from pydispatch import dispatcher

from .handlers import HandlerReservaIntegracion, HandlerReservaComando

from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReserva

dispatcher.connect(HandlerReservaIntegracion.handle_reserva_creada, signal=f'{ReservaCreada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_reserva_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_reserva_pagada, signal=f'{ReservaPagada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_reserva_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')

# comandos
dispatcher.connect(HandlerReservaComando.handle_comando_crear_reserva, signal=f'{ComandoCrearReserva.__name__}')