from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):

    '''
    class facilitates the creation of registration from objects
    '''
    email = StringField('Email',validators=[Required(),Email()])
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required(),EqualTo('confirm_password',message="Both passwords must match")])
    confirm_password = PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def verify_email(self,data_field):

        '''
        function checks if entered email is already in use
        '''
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('The email already exists')
    
    def verify_username(self,data_field):

        '''
        function checks if entered username already exists
        '''
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('The username alredy exists')

class LoginForm(FlaskForm):

    '''
    class facilitates the creation of login form objects
    '''
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')