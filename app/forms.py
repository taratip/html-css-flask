from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User


class PostForm(FlaskForm):
    post = StringField('Tweet...', validators=[DataRequired()])
    submit = SubmitField('Post')


class TitleForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    submit = SubmitField('Change')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age')
    bio = StringField('Bio')
    url = StringField('Profile Pic URL')
    password = PasswordField('Password', validators=[DataRequired()])
    password1 = PasswordField(
        'Re-type Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    # no need to call, system knows that 'validate_' needs to be run
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already taken.')
