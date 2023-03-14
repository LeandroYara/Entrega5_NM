

from entregaAlpes.modulos.envios.dominio.eventos import EnvioCreado
from entregaAlpes.seedwork.aplicacion.handlers import Handler

class HandlerEnvioDominio(Handler):

    @staticmethod
    def handle_envio_creada(evento):
        print('================ ENVIO CREADA ===========')
        

    