from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Email

class TecnicoForm(FlaskForm):
    equipamento = StringField('equipamento', validators=[DataRequired()])
    marca = StringField('marca', validators=[DataRequired()])
    quantidade = SelectField('quantidade', coerce=int, validators=[DataRequired()])
    acessorios = StringField('marca', validators=[DataRequired()])
    observacoes = StringField('marca', validators=[DataRequired()])
    nivel_id = SelectField('Nivel', coerce=int, validators=[DataRequired()])

