from flask_mail import Message
from flask import render_template
from . import mail

subject_pref = 'Partage - '
sender_email = 'watchlist.flask@gmail.com'

def email_message(subject,template,to,**kwargs):

    '''
    function dictates the format of the welcome email that users will receive once they sign up
    '''
    email = Message(subject_pref+subject,sender=sender_email,recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)

def post_email_message(subject,template,to,**kwargs):

    '''
    function dictates update email format
    '''
    email = Message(subject,sender=sender_email,recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
