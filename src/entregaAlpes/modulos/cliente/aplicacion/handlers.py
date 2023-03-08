

from entregaAlpes.modulos.vuelos.dominio.eventos import ReservaCreada
from entregaAlpes.seedwork.aplicacion.handlers import Handler

class HandlerReservaDominio(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        print('================ RESERVA CREADA ===========')
        

    