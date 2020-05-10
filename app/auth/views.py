from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import User
from .. import db
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm
from ..email import email_message

@auth.route('/register')
def register():

    '''
    views function returns the register template and its contents
    '''
    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        user = User(email=register_form.email.data,username=register_form.username.data,password=register_form.password.data)

        db.session.add(user)
        db.session.commit()

        email_message('Welcome To Our Blogging Community','email/welcome_user',user.email, user=user)

        return redirect(url_for('.login'))

        title = 'New Account'

    return render_template("auth/register.html", register_form=register_form)
