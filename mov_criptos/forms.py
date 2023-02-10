from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from mov_criptos.models import *
from config import *
from datetime import date, time
from mov_criptos.connection import Connection

COINS = [('EUR', 'Euro (EUR)'), ('ADA', 'Cardano (ADA)'), ('BNB', 'Binance Coin (BNB)'),
         ('BTC', 'Bitcoin (BTC)'), ('DOT', 'Polkadot (DOT)'), ('ETH', 'Ethereum (ETH)'), 
         ('MATIC', 'MATIC'), ('SOL', 'SOL'), ('USDT', 'Tether (USDT)'), ("XRP", "Ripple (XRP)")]

'''
def CoinsAvailable():
   connect = Connection(f"SELECT moneda_to from registros WHERE moneda_to != 'EUR' GROUP BY moneda_to")
   monedas_rec = connect.res.fetchall()
   COINS_FROM = [("EUR", "Euro (EUR)")]
   for moneda in monedas_rec:
      if moneda[0] == 'BTC':
            COINS_FROM.append(("BTC", "Bitcoin (BTC)"))
      if moneda[0] == 'ETH':
            COINS_FROM.append(("ETH", "Ethereum (ETH)"))
      if moneda[0] == 'USDT':
            COINS_FROM.append(("USDT", "Tether (USDT)"))
      if moneda[0] == 'BNB':
            COINS_FROM.append(("BNB", "Binance Coin (BNB)"))
      if moneda[0] == 'XRP':
            COINS_FROM.append(("XRP", "Ripple (XRP)"))
      if moneda[0] == 'ADA':
            COINS_FROM.append(("ADA", "Cardano (ADA)"))
      if moneda[0] == 'SOL':
            COINS_FROM.append(("SOL", "SOL"))
      if moneda[0] == 'DOT':
            COINS_FROM.append(("DOT", "Polkadot (DOT)"))
      if moneda[0] == 'MATIC':
            COINS_FROM.append(("MATIC", "MATIC"))
   connect.con.commit()
   connect.con.close()
   return COINS_FROM
'''

class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Hora')
   moneda_from = SelectField('Moneda a cambiar', choices=COINS, validators=[DataRequired(message="Selecciona moneda de origen")])
   moneda_to = SelectField('Moneda deseada', choices= COINS, validators=[DataRequired(message="Selecciona moneda deseada")]) 
   
   cantidad_from = FloatField('Cantidad', validators=[DataRequired(message="Ingresa cantidad")])
   calcular = SubmitField('Calcular')
   submit = SubmitField('Realizar transacción')





 