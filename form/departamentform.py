from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class DepartamentForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    chief = IntegerField('Chief', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')