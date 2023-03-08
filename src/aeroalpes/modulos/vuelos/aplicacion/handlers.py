from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from aeroalpes.seedwork.aplicacion.handlers import Handler
from aeroalpes.modulos.vuelos.infraestructura.despachadores import Despachador
from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReservaPayload
from aeroalpes.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearReserva
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReservaDTOJson
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando


class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_reserva_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_reserva_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_reserva_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')


class HandlerReservaComando(Handler):
    @staticmethod
    def handle_comando_crear_reserva(comando: ComandoCrearReservaPayload):
        """
        Comando viene de la capa de infrastructura, creo que se debe transformar a 
        comando CrearReserva de la capa de aplicacion y luego ejecutarlo
        """
        print('##################### COMANDO ####################')
        mapper = MapeadorReservaDTOJson()
        comando_dict = todict(comando)
        reserva = mapper.externo_a_dto(comando_dict)
        comando = CrearReserva(
            id=reserva.id,
            fecha_creacion=reserva.fecha_creacion,
            fecha_actualizacion=reserva.fecha_actualizacion,
            itinerarios=reserva.itinerarios
        )
        ejecutar_commando(comando)


def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj