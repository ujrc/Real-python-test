from flask_wtf import Form
from wtforms import StringField, PasswordField

from wtforms.validators import DataRequired,Length,EqualTo,Email

class RegisterForm(Form):
    name=StringField(
    'Username',
    validators=[DataRequired(),Length(min=6,max=25)])

    email=StringField(
    'Email',
    validators=[DataRequired(), Length(min=6,max=40),Email()])
    password=PasswordField('Password',
    validators=[DataRequired(),Length(min=6,max=40)])
    confirm=PasswordField('Confirm',
    validators=[DataRequired(),Length(min=6,max=40),EqualTo('password')])


class LoginForm(Form):
    name=StringField(
    'Username',    validators=[DataRequired()] )
    password=PasswordField('Password', validators=[DataRequired()])
