from entregaAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
bodegas_items = db.Table(
    "reservas_itinerarios",
    db.Model.metadata,
    db.Column("item_id", db.String, db.ForeignKey("item.id")),
    db.Column("cantidad", db.Integer),
    #db.ForeignKeyConstraint(
        #["odo_orden", "segmento_orden", "leg_orden", "fecha_salida", "fecha_llegada", "origen_codigo", "destino_codigo"],
        #["itinerarios.odo_orden", "itinerarios.segmento_orden", "itinerarios.leg_orden", "itinerarios.fecha_salida", "itinerarios.fecha_llegada", "itinerarios.origen_codigo", "itinerarios.destino_codigo"]
    #)
)
ordenes_items = db.Table(
    "reservas_itinerarios",
    db.Model.metadata,
    db.Column("item_id", db.String, db.ForeignKey("item.id")),
    db.Column("cantidad", db.Integer),
    #db.ForeignKeyConstraint(
        #["odo_orden", "segmento_orden", "leg_orden", "fecha_salida", "fecha_llegada", "origen_codigo", "destino_codigo"],
        #["itinerarios.odo_orden", "itinerarios.segmento_orden", "itinerarios.leg_orden", "itinerarios.fecha_salida", "itinerarios.fecha_llegada", "itinerarios.origen_codigo", "itinerarios.destino_codigo"]
    #)
)
class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    nombre=db.Column(db.String, nullable=False, primary_key=True)

class Bodega(db.Model):
    __tablename__ = "bodega"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    nombre = db.Column(db.String, primary_key=True)
    capacidad= db.Column(db.Integer, primary_key=True)
    latitud=db.Column(db.Float, primary_key=True)
    longitud=db.Column(db.Float, primary_key=True)
    nombre_u = db.Column(db.String, primary_key=True)
    almacenamiento= db.relationship('items', secondary=bodegas_items, backref='bodega')


class Orden(db.Model):
    __tablename__ = "orden"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    itinerarios = db.relationship('items', secondary=ordenes_items, backref='orden')

