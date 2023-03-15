from pydispatch import dispatcher
from entregaAlpes.modulos.sagas.aplicacion.coordinadores.saga_envios import oir_mensaje

dispatcher.connect(oir_mensaje, signal='EnvioCreadoIntegracion')
