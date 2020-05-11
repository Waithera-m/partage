from . import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):

    '''
    function queries and returns user with a given id
    '''
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):

    '''
    class faciliates the creation of user objects
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)
    username = db.Column(db.String(255),index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_photo_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post',backref='user',lazy="dynamic")
    blogs = db.relationship('Blog',backref='user',lazy="dynamic")
    comments = db.relationship('Comments',backref='user',lazy='dynamic')
    
    @property
    def password(self):

        '''
        function blocks access to password property
        '''
        raise AttributeError('Password attribute cannot be read')

    @password.setter
    def password(self,password):

        '''
        function generates password hash
        '''
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self,password):

        '''
        function checks if entered and hashed passwords match
        '''
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):

    '''
    class facilitates the creation of role objects
    '''
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref='role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Blog(db.Model):

    '''
    class facilitates the creation of blog objects
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(70))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tag_id = db.Column(db.Integer,db.ForeignKey('tags.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

class Post(db.Model):

    '''
    class facilitates the creation of post objects
    '''
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(70))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tag_id = db.Column(db.Integer,db.ForeignKey('tags.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comments',backref='post',lazy='dynamic')
    

    @classmethod
    def get_post(cls,id):

        '''
        function queries database and returns pitch with given id
        '''
        post = cls.query.filter_by(id=id).first()
        

        return post



    

class Tag(db.Model):

    '''
    class supports the creation of tag objects
    '''
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(23))
    blogs = db.relationship('Blog',backref = 'tag',lazy='dynamic')
    posts = db.relationship('Post',backref = 'tag',lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

class Quote:

    '''
    class facilitates the creation of quote objects
    '''

    def __init__(self,id,author,quote):
        
        '''
        function facilitates the creation of quote properties

        Args:
            self.id: quote's id
            self.author:quote's author
            self.quote:quote content
        '''
        self.id = id
        self.author = author
        self.quote = quote

class Comments(db.Model):

    '''
    class facilitates the creation of comment objects
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))

    def save_comment(self):

        '''
        function saves comments to the database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):

        '''
        function retrieves post-specific comments
        '''
        comments =  Comments.query.filter_by(post_id=post_id).all()

        return comments

