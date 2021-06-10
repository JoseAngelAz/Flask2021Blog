from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
    validators=[DataRequired(),Email()])
    password = PasswordField('Contraseña',validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#Login Form
class LoginForm(FlaskForm):    
    email = StringField('Correo electronico',
    validators=[DataRequired(),Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    remember = BooleanField('Recuerdame :v')   
    submit = SubmitField('Login')        