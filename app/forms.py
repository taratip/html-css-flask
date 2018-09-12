from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    post = StringField('Tweet...', validators=[DataRequired()])
    submit = SubmitField('Post')

class DataForm(FlaskForm):
    title = StringField('Change Title:', validators=[DataRequired()])
    submit = SubmitField('Change')
