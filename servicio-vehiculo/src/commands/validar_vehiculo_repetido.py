from .base_command import BaseCommannd
from ..models.model_vehiculo import Vehiculo, db

from ..errors.errors import VehiculoyaExiste

class ValidarVehiculoRepetido(BaseCommannd):
    def __init__ (self, marca,  modelo, placa):
        self.marca=marca
        self.modelo=modelo
        self.placa=placa

    def execute(self):
        es_repetido=False

        auto_marca_modelo = Vehiculo.query.filter_by(marca=self.marca,modelo=self.modelo).first()
        auto_marca = Vehiculo.query.filter_by(marca=self.marca).first()
        auto_placa = Vehiculo.query.filter_by(placa=self.placa).first()

        if auto_marca or auto_marca_modelo or auto_placa:
            raise VehiculoyaExiste
        return es_repetido
