class ApiError(Exception):
    code= 422
    description = "API Error"

class InformacionNoValida(ApiError):
    code= 400
    description= "Información Incompleta o no valida"

class InformacionEliminada(ApiError):
    code = 200
    description = 'Todos los datos fueron eliminados'

class VehiculoyaExiste(ApiError):
    code= 412
    description= "El Vehiculo ya existen en el sistema"

class InformacionIncompleta(ApiError):
    code= 400
    description= "Información Incompleta"

class CamposIncompletos(ApiError):
    code= 400
    description= "Campos Incompletos"

class VehiculoNoExiste(ApiError):
    code= 400
    description= "El Vehiculo no existe en la base de datos"


