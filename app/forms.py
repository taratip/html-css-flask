from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User, Role


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    company_name = StringField('Company Name')
    bio = StringField('Bio')
    password = PasswordField('Password', validators=[DataRequired()])
    password1 = PasswordField(
        'Re-type Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    # no need to call, system knows that 'validate_' needs to be run
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already taken.')


class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    company_name = StringField('Company Name')
    bio = StringField('Bio')
    update = SubmitField('Update')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already taken.')


class UserForm(FlaskForm):
    ROLE_TYPES = [(1, 'Admin'), (2, 'User'), (3, 'Partner'), (4, 'Client')]
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    company_name = StringField('Company Name')
    role_id = SelectField('Role', choices=ROLE_TYPES, coerce=int)
    update = SubmitField('Update')
