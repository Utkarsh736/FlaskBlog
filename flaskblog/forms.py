from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

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

    # Validating new account
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is taken. Please choose another username')

    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email is taken. Please choose another email')


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



class UpdateAccountForm(FlaskForm):
    # Username Field
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])

    # Email Field
    email  = StringField('Email',
                        validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    # Submit Field
    submit = SubmitField('Update')

    # Validation for account update
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('That username is taken. Please choose another username')

    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('That email is taken. Please choose another email')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')



class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Reset Password')