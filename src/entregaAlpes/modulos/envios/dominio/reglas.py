"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from entregaAlpes.seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import  Facilitacion


class CantidadMinimaPorProductoFacilitado(ReglaNegocio):

    productos_facilitados: list[Facilitacion]

    def __init__(self, productos_facilitados, mensaje='La cantidad de los productos facilitados debe ser mayor a 0'):
        super().__init__(mensaje)
        self.productos_facilitados = productos_facilitados

    def es_valido(self) -> bool:
        for productos_facilitado in self.productos_facilitados:
            if productos_facilitado.cantidad > 0:
                return True
        return False

class MinimoUnProductoFacilitado(ReglaNegocio):
    productos_facilitados: list[Facilitacion]

    def __init__(self, productos_facilitados, mensaje='La lista de productos facilitados debe tener al menos uno'):
        super().__init__(mensaje)
        self.productos_facilitados = productos_facilitados

    def es_valido(self) -> bool:
        return len(self.productos_facilitados) > 0 and isinstance(self.productos_facilitados[0], Facilitacion) 