# CryptoDanceApp: Registro de movimientos de criptomonedas
Aplicación Web desarrollada en Python con framework Flask y motor de base de datos SQLite.

Proyecto final del Bootcamp 'Full Stack Jr. XIII', de KeepCoding Tech School. 

## Funcionalidad
Se trata de una aplicación para el registro de movimientos de criptomonedas. La idea es comprar, vender o intercambiar criptomonedas para hacer crecer la inversión y obtener beneficios en euros.

La página 'Inicio' muestra todos los movimientos realizados: Compra, venta o intercambio; registrados en una base de datos SQLite.

La página 'Compra' permite realizar una transacción. Iniciando con Euros, se puede invertir en criptomonedas. Una vez se dispone de criptos en cartera, se podrán utilizar como moneda de cambio. El sistema consultará con coinAPI.io para obtener el valor de cambio.

La página 'Estado' muestra la situación de la inversión, los euros gastados en
comprar Bitcoin y el valor actual del total de criptomonedas que existan en la cartera del
usuario según sus movimientos. Si hay ganancia, la cifra en 'Valor Actual' se mostrará en verde; si hay pérdida, se mostrará en rojo. 

La página 'Cartera' muestra el saldo actual de cada criptomoneda posible de obtener con la aplicación. 
  
## Instrucciones de uso:

### En su entorno virtual de python ejecutar el comando:
```
pip install -r requirements.txt
```
### Renombrar el archivo .env_template a .env y agregar:
```
FLASK_APP=main.py
FLASK_DEBUG=true
```
### Renombrar el archivo config_template.py a config.py y agregar:
```
ORIGIN_DATA="data/registros.sqlite"
SECRET_KEY="AGREGA TU CODIGO ENCRIPTADO"
API_KEY="AGREGA TU API KEY UNICA"
```
La ApiKey se obtiene en [www.coinapi.io](https://www.coinapi.io)

### Ejecución con .env:
```
flask run
```

***
## Capturas:
![127 0 0 1_5000_(1366x768)](https://github.com/Vmart1989/movimientos_cripto/assets/87582590/00f8b531-b525-4230-a260-93dff0feef63)
![127 0 0 1_5000_purchase(1366x768)](https://github.com/Vmart1989/movimientos_cripto/assets/87582590/efff8483-96d3-490a-8a69-ef9f706688ed)
![127 0 0 1_5000_status(1366x768)](https://github.com/Vmart1989/movimientos_cripto/assets/87582590/c35f1b49-9f3a-410f-8990-b81cb9d45b95)
![127 0 0 1_5000_wallet(1366x768)](https://github.com/Vmart1989/movimientos_cripto/assets/87582590/8fb64c72-672c-416e-b940-bd11ede74a0f)


