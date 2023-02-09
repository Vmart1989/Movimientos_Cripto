from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from mov_criptos.models import *
from config import *
from datetime import date, time
from mov_criptos.connection import Connection

COINS = [("EUR", "Euro (EUR)"), ("BTC", "Bitcoin (BTC)"), ("ETH", "Ethereum (ETH)"),
           ("USDT", "Tether (USDT)"), ("BNB", "Binance Coin (BNB)"), ("XRP", "Ripple (XRP)"), 
           ("ADA", "Cardano (ADA)"), ("SOL", "SOL"),("DOT", "Polkadot (DOT)"),
           ("MATIC", "MATIC")]

def CoinsAvailable():
   COINS_FROM = ['EUR']
   connect = Connection("SELECT moneda_to from registros")
   monedas_rec = connect.res.fetchall()
   for moneda in monedas_rec:
       if moneda != 'EUR':
         if moneda[0]== 'BTC':
            moneda[0].replace('BTC', 'Bitcoin (BTC)')
         COINS_FROM.append(moneda[0])
         COINS_FROM = list(dict.fromkeys(COINS_FROM))
         
   return COINS_FROM

class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Hora')
   moneda_from = SelectField('Moneda a cambiar', choices=CoinsAvailable(), validators=[DataRequired(message="Selecciona moneda de origen")])
   moneda_to = SelectField('Moneda deseada', choices= COINS, validators=[DataRequired(message="Selecciona moneda deseada")]) 
   
   cantidad_from = FloatField('Cantidad', validators=[DataRequired(message="Ingresa cantidad")])
   calcular = SubmitField('Calcular')
   submit = SubmitField('Realizar transacción')


 