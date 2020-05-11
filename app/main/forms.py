from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required
from ..models import User,Blog,Post,Comments

class EditProfile(FlaskForm):

    '''
    class facilitates the creation of profile form's objects
    '''
    bio = TextAreaField('Let the world know more about you',validators=[Required()])
    submit = SubmitField('Add Bio')

class NewBlog(FlaskForm):

    '''
    class facilitates the creation of blog form's objects
    '''
    title = StringField("Give your blog a title",validators=[Required()])
    submit = SubmitField('Create Blog')

class NewPost(FlaskForm):

    '''
    class facilitates the creation of post form's objects
    '''
    title = StringField('Post Title',validators=[Required()])
    content = TextAreaField('Post Content')
    submit = SubmitField('Add Post')

class NewComments(FlaskForm):

    '''
    class facilitates the creation of comment form's objects
    '''
    comment = TextAreaField('Comment')
    submit = SubmitField('Comment')


    
    
