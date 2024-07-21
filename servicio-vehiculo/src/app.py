from dotenv import load_dotenv
loaded = load_dotenv('.env.development')

from flask import Flask, jsonify
from .blueprints.vehiculo import vehiculos_blueprint
from .errors.errors import ApiError
from flask_sqlalchemy import SQLAlchemy
import os
from .models.model_vehiculo import db

app = Flask(__name__)

#Ajustar el link de la DB segun el despliegue
#Db local userslocal
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/vehiculoslocal'

#DB docker image
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}")
app.config['JWT_SECRET_KEY'] = 'frase-secreta'


#Incluir BluePrint Utilizados
app.register_blueprint(vehiculos_blueprint)

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "msg": err.description,
      #"version": os.environ["VERSION"]
    }
    return jsonify(response), err.code