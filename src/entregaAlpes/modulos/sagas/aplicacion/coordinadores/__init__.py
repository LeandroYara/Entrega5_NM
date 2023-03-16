from pydispatch import dispatcher
from entregaAlpes.modulos.sagas.aplicacion.coordinadores.saga_envios import oir_mensaje

dispatcher.connect(oir_mensaje, signal='EnvioCreadoDominio')
dispatcher.connect(oir_mensaje, signal='EnvioCourierDefinidoDominio')
dispatcher.connect(oir_mensaje, signal='EnvioCourierConfirmadaDominio')
dispatcher.connect(oir_mensaje, signal='ConfirmacionDeCourierFallidaDominio')
dispatcher.connect(oir_mensaje, signal='AsignacionDeCourierFallidaDominio')