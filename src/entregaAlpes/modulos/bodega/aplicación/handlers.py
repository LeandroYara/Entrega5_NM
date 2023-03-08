from entregaAlpes.modulos.bodega.dominio.eventos import ordenCreada, ordenCancelada, ordenAprobada, ordenPagada
from entregaAlpes.seedwork.aplicacion.handlers import Handler
from entregaAlpes.modulos.bodega.infraestructura.despachador import Despachador

class HandlerordenIntegracion(Handler):

    @staticmethod
    def handle_orden_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden')

    @staticmethod
    def handle_orden_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden')

    @staticmethod
    def handle_orden_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden')

    @staticmethod
    def handle_orden_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden')


    