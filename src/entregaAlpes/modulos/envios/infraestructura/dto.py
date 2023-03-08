"""DTOs para la capa de infrastructura del dominio de envios

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de envios

"""

from entregaAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

facilitaciones = db.Table(
    "envios_facilitaciones",
    db.Model.metadata,
    db.Column("envio_id", db.Integer, db.ForeignKey("envios.id")),
    db.Column("producto_nombre", db.String),
    db.Column("centro_distribucion", db.String),
    db.Column("centro_distribucion_direccion", db.String),
    db.Column("cantidad", db.Integer),
    db.ForeignKeyConstraint(
        ["envio_id", "producto_nombre", "centro_distribucion", "centro_distribucion_direccion", "courier_nombre", "cantidad"],
    )
)

class Facilitacion(db.Model):
    __tablename__ = "facilitaciones"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    producto_nombre = db.Column(db.String, nullable=False, primary_key=True)
    centro_distribucion = db.Column(db.String, nullable=False, primary_key=True)
    centro_distribucion_direccion = db.Column(db.String, nullable=False, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False, primary_key=True)


class Envio(db.Model):
    __tablename__ = "envios"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    courier_nombre = db.Column(db.String, nullable=False, primary_key=True)
    destino_nombre = db.Column(db.String, nullable=False, primary_key=True)
    destino_direccion = db.Column(db.String, nullable=False, primary_key=True)
    facilitaciones = db.relationship('Facilitacion', secondary=facilitaciones, backref='envios')
