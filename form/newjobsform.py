from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Job Title', validators=[DataRequired()])
    team_leader = IntegerField('Team leader id', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    category = SelectMultipleField('Hazard category', validators=[DataRequired()], coerce=int)
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Submit')
