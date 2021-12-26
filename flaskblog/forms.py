from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Registration Form

class RegistrationForm(FlaskForm):
    # Username Field
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])

    # Email Field
    email  = StringField('Email',
                        validators=[DataRequired(), Email()])

    # Password and confirm password
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])

    
    # Submit Field
    submit = SubmitField('Sign Up')


# Login Form

class LoginForm(FlaskForm):
    # Email Field
    email  = StringField('Email',
                        validators=[DataRequired(), Email()])

    # Password and confirm password
    password = PasswordField('Password', validators=[DataRequired()])

    # Save cookie
    remember = BooleanField('Remember Me')

    # Submit Field
    submit = SubmitField('Login')
