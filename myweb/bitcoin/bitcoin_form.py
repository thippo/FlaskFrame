from flask_wtf import Form
from wtforms import RadioField, IntegerField, SelectField, TextField
from wtforms.validators import DataRequired, Required

class SearchForm(Form):
    q = TextField(validators=[Required()])