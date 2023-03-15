"""DTOs para la capa de infrastructura del dominio de envios

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de envios

"""

from entregaAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

envios_facilitaciones = db.Table(
    "envios_facilitaciones",
    db.Model.metadata,
    db.Column("envio_id", db.String(40), db.ForeignKey("envios.id")),
    db.Column("id_pedido", db.String(40)),
    db.Column("producto_nombre", db.String(250)),
    db.Column("centro_distribucion", db.String(250)),
    db.Column("centro_distribucion_direccion", db.String(250)),
    db.Column("cantidad", db.Integer),
    db.ForeignKeyConstraint(
        ["id_pedido", "producto_nombre", "centro_distribucion", "centro_distribucion_direccion", "cantidad"],
        ["facilitaciones.id_pedido", "facilitaciones.producto_nombre", "facilitaciones.centro_distribucion",
        "facilitaciones.centro_distribucion_direccion", "facilitaciones.cantidad"],
    )
)

class Facilitacion(db.Model):
    __tablename__ = "facilitaciones"
    id_pedido = db.Column(db.String(40), primary_key=True)
    producto_nombre = db.Column(db.String(250), nullable=False, primary_key=True)
    centro_distribucion = db.Column(db.String(250), nullable=False, primary_key=True)
    centro_distribucion_direccion = db.Column(db.String(250), nullable=False, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False, primary_key=True)


class Envio(db.Model):
    __tablename__ = "envios"
    id = db.Column(db.String(40), primary_key=True)
    id_pedido = db.Column(db.String(40), primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    courier_nombre = db.Column(db.String(250), nullable=True)
    destino_nombre = db.Column(db.String(250), nullable=False)
    destino_direccion = db.Column(db.String(250), nullable=False)
    facilitaciones = db.relationship('Facilitacion', secondary=envios_facilitaciones, backref='envios')


class EventosEnvio(db.Model):
    __tablename__ = "eventos_envios"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)


# TODO: mover a microservicio logistica_envio
# No debe tener ForeignKey a Envio
class LogisticaEnvio(db.Model):
    __tablename__ = "logistica_envios"
    id = db.Column(db.String(40), primary_key=True)
    id_pedido = db.Column(db.String(40), primary_key=True)
    courier_nombre = db.Column(db.String(250), nullable=True)
    is_externo = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
