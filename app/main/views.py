from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from ..models import User, Post,Comment, UpVote, DownVote
from flask_login import login_required, current_user
from .. import db, photos
from .forms import AddPostForm, AddComment, UpdateProfile

@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    '''
    title = "Welcome | FarmOverflow"


    return render_template("index.html", title=title)
@main.route('/home')
def home():
    '''
    root page function that returns the index page and its data
    '''
    title = "Welcome | FarmOverflow"
    posts = Post.query.order_by(Post.time.desc())


    return render_template("home.html", title=title, posts=posts)

@main.route("/add/post/",methods = ["GET","POST"])
@login_required
def add_post():
    form = AddPostForm()
    title = "Add Post"

    print(form)
    if form.validate_on_submit():
        post = form.post.data
        
        new_post = Post(user_id = current_user.id, post = post)
        
        db.session.add(new_post)
        db.session.commit()
        emails = []
        title = 'New Post'
        
        return redirect(url_for('main.home'))

    return render_template("add_pitch.html",form = form,title = title)

@main.route("/post/<int:id>",methods = ["GET","POST"])
@login_required
def post_page(id):
    post = Post.query.filter_by(id = id).first()
    form = AddComment()
    comment = Comment.query.filter_by(id = id).first()
    # post_id = comment.post.id

    if id is None:
        abort(404)

    if form.validate_on_submit():
        # name = form.username.data
        content = form.comment.data
        new_comment = Comment(content = content, post = post, user = current_user)
        new_comment.save_comment()
        return redirect(url_for('main.post_page', id = post.id))
    all_comments = Comment.get_comments(id)   
    title = 'FARMOVERFLOW | CONVERSATIONS'
    up_likes = UpVote.get_votes(id)
    down_likes = DownVote.get_downvotes(id)
    # comments = Comment.query.filter_by(post_id = post.id)
    return render_template("post.html", title = title, post = post,form = form, comments=all_comments, likes = up_likes, dislikes=down_likes)

@main.route("/delete/<id>")
def delete(id):
    post = Post.query.filter_by(id = id).first()
    user_id = post.user_id
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.profile', id = user_id))

@main.route("/delete/comment/<id>")
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.post_page", id = post_id))

@main.route("/profile/<id>")
@login_required
def profile(id):
    user = User.query.filter_by(id = id).first()
    
    posts = Post.query.filter_by(user_id = user.id).order_by(Post.time.desc())
    title = user.username
    return render_template("profile.html", user = user,posts = posts, title = title)

@main.route("/<user_id>/profile/edit",methods = ["GET","POST"])
@login_required
def update_profile(user_id):
    title = "Edit Profile"
    user = User.query.filter_by(id = user_id).first()
    form = UpdateProfile()

    if form.validate_on_submit():
        bio = form.bio.data
        user.bio = bio
        db.session.commit() 
        return redirect(url_for('main.profile',id = user.id)) 
    return render_template("update_profile.html",form = form,title = title)

@main.route("/pic/<user_id>/update", methods = ["POST"])
@login_required
def update_pic(user_id):
    user = User.query.filter_by(id = user_id).first()
    title = "Edit Profile"
    if "profile-pic" in request.files:
        pic = photos.save(request.files["profile-pic"])
        file_path = f"photos/{pic}"
        user.image = file_path
        db.session.commit()
    return redirect(url_for("main.profile", id = current_user.id))

@main.route('/home/like/<int:id>', methods = ['GET','POST'])
@login_required
def like(id):
    get_pitches = UpVote.get_votes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.post_page',id=id))
        else:
            continue

    like_post = UpVote(user = current_user, posting_id=id)
    like_post.save_vote()

    return redirect(url_for('main.post_page',id=id))

@main.route('/home/dislike/<int:id>', methods = ['GET','POST'])
@login_required
def dislike(id):
    get_pitches = DownVote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.post_page',id=id))
        else:
            continue

    dislike_post = DownVote(user = current_user, posting_id=id)
    dislike_post.save_vote()

    return redirect(url_for('main.post_page',id=id))

@main.route('/user/<username>&<id_user>')
@login_required
def profiles(username, id_user):
    user = User.query.filter_by(username = username).first()

    title = f"{username.capitalize()}'s Profile"

    get_posts = Post.query.filter_by(user_id = id_user).all()
    get_comments = Comment.query.filter_by(user_id = id_user).all()
    get_upvotes = UpVote.query.filter_by(id_user = id_user).all()
    get_downvotes = DownVote.query.filter_by(id_user = id_user).all()

    if user is None:
        abort(404)
    
    return render_template('profile.html', user = user, title=title, posts_no = get_posts, comments_no = get_comments, likes_no = get_upvotes, dislikes_no = get_downvotes)
