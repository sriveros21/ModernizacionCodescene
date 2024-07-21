from .base_command import BaseCommannd
#Pendiente configurar los errores
from ..models.model_vehiculo import Vehiculo,db
from ..errors.errors import InformacionIncompleta
import datetime
import uuid
import os
import re

class CrearVehiculo(BaseCommannd):
    def __init__ (self,cilindraje,color,kilometraje,marca, modelo,placa,tipo_combustible):
        self.cilindraje= cilindraje
        self.color= color
        self.kilometraje= kilometraje
        self.marca= marca
        self.modelo= modelo
        self.placa= placa
        self.tipo_combustible= tipo_combustible

    def execute(self):

        #Definir campos mandatorios
        if not all ([self.cilindraje,self.color,self.kilometraje,self.marca, self.modelo,self.placa,self.tipo_combustible]):
           raise InformacionIncompleta

        vehiculo=Vehiculo(cilindraje=self.cilindraje,color=self.color,estado=False,kilometrajeCompra=self.kilometraje,marca=self.marca,modelo=self.modelo,placa=self.placa,tipoCombustible=self.tipo_combustible)        
        
        db.session.add(vehiculo)
        db.session.commit()

        return vehiculo