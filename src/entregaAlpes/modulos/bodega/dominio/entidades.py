from datetime import datetime
from entregaAlpes.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field
import entregaAlpes.modulos.bodega.dominio.objetos_valor as ov
from .objetos_valor import Nombre, Capacidad, Ubicacion
from entregaAlpes.modulos.bodega.dominio.eventos import *

@dataclass(frozen=True)
class Item(Entidad):
    nombre: str
@dataclass(frozen=True)
class Group(Entidad):
    cantidad: int
    item: Item
@dataclass
class Bodega(Entidad):
    nombre: Nombre=field(default_factory=Nombre)
    capacidad: Capacidad=field(default_factory=Capacidad)
    ubicacion: Ubicacion=field(default_factory=Ubicacion)
    almacenamiento: list[ov.Group]=field(default_factory=list[ov.Group]) 
    
@dataclass
class Orden(AgregacionRaiz):
    estado: ov.EstadoOrden = field(default=ov.EstadoOrden.PENDIENTE)
    #itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])
    #Si la orden tiene varios productos todos tienen que llegar
    def crear_orden(self, orden: Orden):
        self.id_cliente = orden.id_cliente
        self.estado = orden.estado
        self.itinerarios = orden.itinerarios

        self.agregar_evento(OrdenCreada(id_Orden=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def aprobar_orden(self):
        self.estado = ov.EstadoOrden.APROBADA

        self.agregar_evento(OrdenAprobada(self.id, self.fecha_actualizacion))

    def cancelar_orden(self):
        self.estado = ov.EstadoOrden.CANCELADA

        self.agregar_evento(OrdenCancelada(self.id, self.fecha_actualizacion))
    
