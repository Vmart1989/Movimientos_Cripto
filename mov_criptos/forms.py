from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from mov_criptos.models import *
from config import *
from datetime import date, time

COINS = [("EUR", "Euro"), ("BTC", "Bitcoin"), ("ETH", "Ethereum"),
           ("USDT", "Tether"), ("BNB", "Binance Coin"), ("XRP", "Ripple"), 
           ("ADA", "Cardano"), ("SOL", "SOL"),("DOT", "Polkadot"),
           ("MATIC", "MATIC")]

class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Hora')
   moneda_from = SelectField('Moneda a cambiar', choices=COINS, validators=[DataRequired(message="Selecciona moneda de origen")])
   moneda_to = SelectField('Moneda deseada', choices= COINS, validators=[DataRequired(message="Selecciona moneda deseada")]) 
   
   cantidad_from = FloatField('Cantidad', validators=[DataRequired(message="Ingresa cantidad")])
   calcular = SubmitField('Calcular')
   submit = SubmitField('Realizar transacción')


 