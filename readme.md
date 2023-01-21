# Aplicación web: Registro de movimientos de criptomonedas
Web App hecha en python con el framework Flask, y con motor de base de datos SQLite    
  
## Instrucciones de uso:

### En su entorno virtual de python ejecutar el comando:
```
pip install -r requirements.txt
```
La librería utilizada es [Flask](https://flask.palletsprojects.com/en/2.2.x/)
### Renombrar el archivo .env_template a .env y agregar:
```
FLASK_APP=main.py
FLASK_DEBUG=true
```
### Renombrar el archivo config_template.py a config.py y agregar:
```
ORIGIN_DATA="data/movimientos.sqlite"
SECRET_KEY="AGREGA TU CODIGO ENCRIPTADO"
API_KEY="AGREGA TU API KEY UNICA"
```
### Ejecución con .env:
```
flask run
```
