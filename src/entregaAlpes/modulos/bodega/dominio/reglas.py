
from entregaAlpes.seedwork.dominio.reglas import ReglaNegocio
from entregaAlpes.modulos.bodega.dominio.entidades import Bodega

class StockBodegaMayor0(ReglaNegocio):
    bodega:Bodega

    def __init__(self, bodega, mensaje='La bodega no puede sacar elementos si no tiene estos'):
        super().__init__(mensaje)
        self.bodega = bodega

"""    def es_valido(self) -> bool:
        return len(self.itinerarios) > 0 and isinstance(self.itinerarios[0], Itinerario) """
#Aun es necesario definir el como se va a hacer esto dado que la estructura no la tengo clara
class DisponibilidadBodega():
    def __init__(self, bodega, mensaje='La bodega no puede guardar elementos si no tiene espacio'):
        super().__init__(mensaje)
        self.bodega = bodega