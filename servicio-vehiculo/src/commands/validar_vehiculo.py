from .base_command import BaseCommannd

from ..errors.errors import InformacionNoValida

class ValidarVehiculo(BaseCommannd):
    def __init__ (self, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
        self.marca=marca
        self.placa=placa
        self.modelo=modelo
        self.kilometraje=kilometraje
        self.color=color
        self.cilindraje =cilindraje 
        self.tipo_combustible =tipo_combustible

    def execute(self):
        es_valido=False
        try:
            if str(self.marca) and str(self.placa) and int(self.modelo) \
                    and int(self.kilometraje) and str(self.color) and float(self.cilindraje) \
                    and str(self.tipo_combustible):
                if int(self.kilometraje) > 0 and float(self.cilindraje) > 0:
                    es_valido = True
        except ValueError:
            raise InformacionNoValida
        
        return es_valido










