from pydispatch import dispatcher
from entregaAlpes.modulos.logistica_envios.infraestructura.consumidores import suscribirse_a_comandos

dispatcher.connect(suscribirse_a_comandos, signal='EnvioCreadoIntegracion')
