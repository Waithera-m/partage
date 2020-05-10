from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required
from ..models import User,Blog

class EditProfile(FlaskForm):

    '''
    class facilitates the creation of profile form objects
    '''
    bio = TextAreaField('Let the world know more about you',validators=[Required()])
    submit = SubmitField('Add Bio')

class NewBlog(FlaskForm):

    '''
    class facilitates the creation of profile form objects
    '''
    title = StringField("Give your blog a title",validators=[Required()])
    submit = SubmitField('Create Blog')
    
    
