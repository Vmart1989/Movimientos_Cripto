from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, TimeField, SelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from mov_criptos.models import *

class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Fecha')
   moneda_from = StringField('Moneda de cambio')
   moneda_to = StringField('Moneda deseada')
   cantidad_from = FloatField('Cantidad', validators=[DataRequired(message="Ingresa cantidad")])
   
   calcular = SubmitField('Calcular')
   
   cantidad_to = FloatField('Valor de cambio actual')

   p_u = StringField('Precio Unitario')
   
   submit = SubmitField('Realizar transacción')
