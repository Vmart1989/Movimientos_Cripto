from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, ValidationError, InputRequired
from mov_criptos.models import *
from config import *
COINS = [("EUR", "Euro"), ("BTC", "Bitcoin"), ("ETH", "Ethereum"),
           ("USDT", "Tether"), ("BNB", "Binance Coin"), ("XRP", "Ripple"), 
           ("ADA", "Cardano"), ("SOL", "SOL"),("DOT", "Polkadot"),
           ("MATIC", "MATIC")]


class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Hora')
   moneda_from = SelectField('Moneda a cambiar', choices=COINS, validators=[DataRequired(message="Selecciona moneda de origen")])
   moneda_to = SelectField('Moneda deseada', choices=COINS, validators=[DataRequired(message="Selecciona moneda deseada")]) 
   cantidad_from = FloatField('Cantidad', validators=[DataRequired(message="Ingresa cantidad")])
   calcular = SubmitField('Calcular')
   submit = SubmitField('Realizar transacción')

   def validate_moneda_to(moneda_from, moneda_to):
      if moneda_to == moneda_from:
         raise ValidationError("Los campos Moneda a cambiar y Moneda deseada no pueden ser iguales")