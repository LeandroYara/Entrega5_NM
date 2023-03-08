from entregaAlpes.seedwork.aplicacion.queries import QueryHandler
from entregaAlpes.modulos.solicitudes.infraestructura.fabricas import FabricaVista
from entregaAlpes.modulos.solicitudes.dominio.fabricas import FabricaEnvios

class SolicitudQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_envios: FabricaEnvios = FabricaEnvios()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_envios(self):
        return self._fabrica_envios    