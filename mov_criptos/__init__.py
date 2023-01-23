from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config") #para que reconozca la clave secreta desde config.py

from mov_criptos.routes import *