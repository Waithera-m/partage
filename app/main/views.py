from flask import render_template,request,url_for,jsonify
from . import main
from ..models import Blog
# from ..request import get_quote

@main.route('/')
def index():

    '''
    view function returns index template and its contents
    '''
    title='Partage'

    # random_quote = get_quote()
    
    
    return render_template('index.html',title=title)


    
