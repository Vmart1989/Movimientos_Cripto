from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, TimeField, SelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError

class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Fecha')
   moneda_from = SelectMultipleField('Moneda a cambiar', choices=[('EUR'), ('BTC'), ('ETH'),('USDT'), ('BNB'), ('XRP'),('ADA'), ('SOL'), ('DOT'),('MATIC')])
   moneda_to = SelectMultipleField('Moneda deseada', choices=[('EUR'), ('BTC'), ('ETH'),('USDT'), ('BNB'), ('XRP'),('ADA'), ('SOL'), ('DOT'),('MATIC')])
   cantidad_from = FloatField('Cantidad', validators=[DataRequired(message="Ingresa cantidad")])
   calcular = SubmitField('Calcular')
   
   cantidad_to = FloatField('Valor de cambio actual')

   p_u = StringField('Precio Unitario')
   
   submit = SubmitField('Realizar transacción')
