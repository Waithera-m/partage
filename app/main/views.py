from flask import render_template,request,url_for
from . import main

@main.route('/')
def index():

    '''
    view function returns index template and its contents
    '''
    title='Partage'
    
    return render_template('index.html',title=title)
