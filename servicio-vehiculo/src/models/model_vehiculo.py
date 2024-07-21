from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, MetaData, text, Enum
from sqlalchemy.orm import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import enum

db= SQLAlchemy()


class Vehiculo (db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    cilindraje=db.Column(db.Float,nullable=False)
    color=db.Column(db.String,nullable=False)
    estado=db.Column(db.Boolean)
    kilometrajeCompra=db.Column(db.Integer,nullable=False)
    kilometrajeVenta=db.Column(db.Integer)
    marca=db.Column(db.String,nullable=False)
    modelo=db.Column(db.Integer,nullable=False)
    placa=db.Column(db.String,nullable=False)
    precioVenta=db.Column(db.Float)
    tipoCombustible=db.Column(db.String,nullable=False)


class VehiculoSchema(SQLAlchemyAutoSchema):
    id = fields.String()
    cilindraje = fields.Float()
    color = fields.String()
    estado = fields.Boolean()
    kilometrajeCompra = fields.Integer()
    kilometrajeVenta = fields.Integer()
    marca = fields.String()
    modelo = fields.Integer()
    placa = fields.String()
    precioVenta = fields.Float()
    tipoCombustible = fields.String()

    class Meta:
        model = Vehiculo
        load_instance = True

    data = fields.Raw(load_only=True)