from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, TimeField
from wtforms.validators import DataRequired, Length, ValidationError

class RegistrosForm(FlaskForm):
   date = DateField('Fecha')
   time = TimeField('Fecha')
   moneda_from = StringField('From', validators=[DataRequired(message="Elige moneda")])
   moneda_to = StringField('To', validators=[DataRequired(message="Elige moneda")])
   cantidad_from = FloatField('Cantidad From', validators=[DataRequired(message="Ingresa cantidad")])
   
   calcular = SubmitField('Calcular')
   
   cantidad_to = FloatField('Cantidad To')

   p_u = StringField('Precio Unitario')
   
   submit = SubmitField('Aceptar')
