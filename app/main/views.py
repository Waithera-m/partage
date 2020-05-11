from flask import render_template,request,url_for,abort,redirect
from . import main
from ..models import User,Blog,Post,Comments
from .. import db,photos
from flask_login import login_required,current_user
from .forms import EditProfile,NewBlog,NewPost,NewComments
import markdown2
# from ..request import get_quote

@main.route('/')
def index():

    '''
    view function returns index template and its contents
    '''
    title='Partage'

    # random_quote = get_quote()
    
    
    return render_template('index.html',title=title)

@main.route('/user/<uname>')
def profile(uname):

    '''
    view function renders user's profile page
    '''
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html",user=user)

@main.route('/user/<uname>/update', methods=["GET","POST"])
@login_required
def edit_profile(uname):

    '''
    view function renders edit profile template
    '''
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    
    form = EditProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/edit.html',form=form)

@main.route('/user/<uname>/update/pic', methods=["POST"])
@login_required
def update_pic(uname):

    '''
    view function facilitates the processing of form submission request
    '''
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_photo_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/blog/new',methods=["GET","POST"])
@login_required
def new_blog():

    '''
    view function returns new blog template and its contents
    '''
    blog_form = NewBlog()

    if blog_form.validate_on_submit():
        title = blog_form.title.data
        new_blog = Blog(title=title, user=current_user)

        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    
    title = "New Blog"
    return render_template('new_blog.html',title=title,blog_form=blog_form)



@main.route('/post/new',methods=["GET","POST"])
@login_required
def new_post():

    '''
    view function returns new blog template and its contents
    '''
    post_form = NewPost()

    if post_form.validate_on_submit():
        title = post_form.title.data
        content = post_form.content.data
        new_post = Post(title=title,content=content,user=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    title = "New Post"
    return render_template('new_post.html',title=title,post_form=post_form)

@main.route('/post/<int:id>',methods=["GET","POST"])
def single_post(id):

    '''
    View function returns transformed markdwon textarea
    '''
    post = Post.get_post(id)
    post_id = post.id

    if post is None:
        abort(404)

    comment_form = NewComments()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        user = current_user
        new_comment = Comments(comment=comment,user=user,post_id=post.id)

        new_comment.save_comment()

        return redirect("/post/{post_id}".format(post_id=post.id))
    comments = Comments.get_comments(post_id)

    format_post = markdown2.markdown(post.content,extras=["code-friendly","fenced-code-blocks"])
    
    return render_template('post.html',post=post,format_post=format_post,user=current_user,comments=comments,comment_form=comment_form)

@main.route('/user/<uname>/posts')
def registered_posts(uname):


    '''
    view function returns all posts added by a particular user
    '''
    user = User.query.filter_by(username=uname).first()
    posts = Post.query.filter_by(user_id=user.id).all()

    return render_template('profile/blog_posts.html',user=user,posts=posts)

@main.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
    
