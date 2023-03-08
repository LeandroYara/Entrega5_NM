from entregaAlpes.seedwork.aplicacion.comandos import ComandoHandler
from entregaAlpes.modulos.envios.infraestructura.fabricas import FabricaRepositorio
from entregaAlpes.modulos.envios.dominio.fabricas import FabricaEnvios

class EnvioBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_envios: FabricaEnvios = FabricaEnvios()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_envios(self):
        return self._fabrica_envios    
    