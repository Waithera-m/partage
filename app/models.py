from . import db
from datetime import datetime

class Blog(db.Model):

    '''
    class facilitates the creation of blog objects
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(70))
    content = db.Column(db.Text)
    blog_photo = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tag_id = db.Column(db.Integer,db.ForeignKey('tags.id'))

    @property
    def serialize(self):

        '''
        function facilitates the return of data in JSON format
        '''
        return {
            'id':self.id,
            'title':self.title,
            'content':self.content,
            'blog_photo':self.blog_photo,
            'created_at':self.created_at,
        }

class Tag(db.Model):

    '''
    class supports the creation of tag objects
    '''
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(23))
    blogs = db.Relationship('Blog',backref = 'tag',lazy='dynamic')

    @property
    def serialize(self):

        '''
        function facilitates the return of data in JSON format
        '''
        return {
            'id': self.id,
            'name': self.name,
        }

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


