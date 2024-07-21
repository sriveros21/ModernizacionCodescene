from .base_command import BaseCommannd
#Pendiente configurar los errores
from ..models.model_vehiculo import Vehiculo,db
from ..errors.errors import InformacionIncompleta
import datetime
import uuid
import os
import re

class ActualizarVehiculo(BaseCommannd):
    def __init__ (self,cilindraje,color,kilometraje,marca, modelo,placa,tipo_combustible,id):
        self.cilindraje= cilindraje
        self.color= color
        self.kilometraje= kilometraje
        self.marca= marca
        self.modelo= modelo
        self.placa= placa
        self.tipo_combustible= tipo_combustible
        self.id=id

    def execute(self):

        #Definir campos mandatorios
        if not all ([self.cilindraje,self.color,self.kilometraje,self.marca, self.modelo,self.placa,self.tipo_combustible]):
           raise InformacionIncompleta
        
        vehiculo =Vehiculo.query.get(self.id)

        vehiculo.marca=self.marca
        vehiculo.placa=self.placa
        vehiculo.modelo=self.modelo
        vehiculo.kilometrajeCompra=self.kilometraje
        vehiculo.color=self.color
        vehiculo.cilindraje=self.cilindraje
        vehiculo.tipoCombustible=self.tipo_combustible

        db.session.commit()

        return vehiculo