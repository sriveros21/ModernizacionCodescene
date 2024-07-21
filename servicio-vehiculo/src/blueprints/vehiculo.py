from flask import Flask, jsonify, request, Blueprint, g
import os
import requests
from ..models.model_vehiculo import db, Vehiculo, VehiculoSchema
from ..errors.errors import CamposIncompletos, VehiculoNoExiste
from ..commands.validar_vehiculo import ValidarVehiculo
from ..commands.validar_vehiculo_repetido import ValidarVehiculoRepetido
from ..commands.crear_vehiculo import CrearVehiculo
from ..commands.actualizar_vehiculos import ActualizarVehiculo
from ..commands.db_restore import db_restore
from datetime import datetime

vehiculo_schema =VehiculoSchema()

vehiculos_blueprint = Blueprint('vehiculos', __name__)

#Consulta de salud del servicio
@vehiculos_blueprint.route('/vehiculos/ping', methods =['GET'])

def salud_servicio():
    return jsonify({'body':"pong"},200)


#Creación de Vehiculos
@vehiculos_blueprint.route('/vehiculos', methods =['POST'])

def crear_vehiculo():
    data = request.json
    if all (fields in data for fields in ("marca","placa", "modelo", "kilometraje", "color","cilindraje", "tipo_combustible")):
        
        command_val = ValidarVehiculo(marca=data["marca"], placa=data["placa"], 
                               modelo=data["modelo"], kilometraje=data["kilometraje"],
                               color=data["color"], cilindraje=data["cilindraje"],tipo_combustible=data["tipo_combustible"])
        command_val.execute()

        command_dup = ValidarVehiculoRepetido(marca=data["marca"], placa=data["placa"], 
                               modelo=data["modelo"])
        command_dup.execute()
        
        command_create = CrearVehiculo(marca=data["marca"], placa=data["placa"], 
                               modelo=data["modelo"], kilometraje=data["kilometraje"],
                               color=data["color"], cilindraje=data["cilindraje"],tipo_combustible=data["tipo_combustible"])       

        vehiculo = command_create.execute()

        return jsonify(id=vehiculo.id, marca=vehiculo.marca, modelo=vehiculo.modelo), 201
    else:
        raise CamposIncompletos
    
#Actualizar Vehiculo
@vehiculos_blueprint.route('/vehiculos/<string:id>', methods =['PUT'])
def actualizar_vehiculo(id):

    data = request.json
    if all (fields in data for fields in ("marca","placa", "modelo", "kilometraje", "color","cilindraje", "tipo_combustible")):
        
        command_val = ValidarVehiculo(marca=data["marca"], placa=data["placa"], 
                               modelo=data["modelo"], kilometraje=data["kilometraje"],
                               color=data["color"], cilindraje=data["cilindraje"],tipo_combustible=data["tipo_combustible"])
        command_val.execute()

        command_update = ActualizarVehiculo(marca=data["marca"], placa=data["placa"], 
                               modelo=data["modelo"], kilometraje=data["kilometraje"],
                               color=data["color"], cilindraje=data["cilindraje"],tipo_combustible=data["tipo_combustible"], id=id)       

        vehiculo = command_update.execute()

        return [vehiculo_schema.dump(vehiculo)]

    else:
        raise CamposIncompletos


#Obtener Vehiculo
@vehiculos_blueprint.route('/vehiculos/<string:id>', methods =['GET'])
def obtener_vehiculo(id):
    vehiculo =Vehiculo.query.get(id)
    if not vehiculo:
        raise VehiculoNoExiste
    return [vehiculo_schema.dump(vehiculo)]

#Listar Vehiculos en DB

@vehiculos_blueprint.route('/vehiculos', methods =['GET'])
def listar_vehiculos():
    vehiculos =Vehiculo.query.all()
    return [vehiculo_schema.dump(vehiculo) for vehiculo in vehiculos]

#Borrar Vehiculo

@vehiculos_blueprint.route('/vehiculos/<string:id>', methods=['DELETE'])
def borrar_vehiculo(id):
    vehiculo = Vehiculo.query.get(id)
    if not vehiculo:
        raise VehiculoNoExiste
    db.session.delete(vehiculo)
    db.session.commit()
    return "Vehículo borrado exitosamente", 200



#Restablecer base de datos  
@vehiculos_blueprint.route('/vehiculos/reset', methods =['POST'])
def clear_data():
    db_restore.execute()
    return jsonify({'msg':"OK"},200)
