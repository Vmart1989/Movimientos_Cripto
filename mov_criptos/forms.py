from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired
from mov_criptos.models import *
from config import *

COINS = [('EUR', 'Euro (EUR)'), ('ADA', 'Cardano (ADA)'), ('BNB', 'Binance Coin (BNB)'),
         ('BTC', 'Bitcoin (BTC)'), ('DOT', 'Polkadot (DOT)'), ('ETH', 'Ethereum (ETH)'), 
         ('MATIC', 'Polygon (MATIC)'), ('SOL', 'Solana (SOL)'), ('USDT', 'Tether (USDT)'), ("XRP", "XRP (XRP)")]

class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Hora')
   moneda_from = SelectField('Moneda a cambiar', choices=COINS, validators=[DataRequired(message="Selecciona moneda de origen")])
   moneda_to = SelectField('Moneda deseada', choices= COINS, validators=[DataRequired(message="Selecciona moneda deseada")]) 
   cantidad_from = FloatField('Cantidad', validators=[DataRequired(message="Ingresa cantidad")])
   calcular = SubmitField('Calcular')
   submit = SubmitField('Realizar transacción')





 