from . import db
from flask_login import UserMixin
from app import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from time import time

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin,db.Model):
    """
    Class  to create users
    """
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(40),unique = True, index=True)
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String)
    image = db.Column(db.String(255))
    posts = db.relationship("Post", backref = "user", lazy = "dynamic")
    user_pass = db.Column(db.String)

    comments = db.relationship('Comment',backref='user',lazy='dynamic')
    upvotes = db.relationship('UpVote',backref='user',lazy='dynamic')
    downvotes = db.relationship('DownVote',backref='user',lazy='dynamic')
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError("Gerrarahia")

    @password.setter
    def password(self,password):
        self.user_pass = generate_password_hash(password)

    def verify_pass(self,password):
        return check_password_hash(self.user_pass, password)

    def __repr__(self):
       return f'User {self.username}'
class Post(db.Model):
    __tablename__ = "posts"
    id  = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post = db.Column(db.String)
    time = db.Column(db.String)
    comments = db.relationship("Comment",backref = "post", lazy = "dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls,id):
        posts = Post.query.filter_by(id=id).all()
        return posts

    @classmethod
    def get_all_posts(cls):
        posts = Post.query.order_by('-id').all()
        return posts

    def get_post_comments(self):
        comments= Comment.query.filter_by(post_id = self.id)
        return comments

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    content = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    time = db.Column(db.String)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments
class UpVote(db.Model):
   __tablename__ = 'upvotes'

   id = db.Column(db.Integer,primary_key=True)
   id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
   posting_id = db.Column(db.Integer)

   def save_vote(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_votes(cls,id):
       upvote = UpVote.query.filter_by(posting_id=id).all()
       return upvote

   def __repr__(self):
       return f'{self.id_user}:{self.posting_id}'


class DownVote(db.Model):
   __tablename__ = 'downvotes'

   id = db.Column(db.Integer,primary_key=True)
   id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
   posting_id = db.Column(db.Integer)

   def save_vote(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_downvotes(cls,id):
       downvote = DownVote.query.filter_by(posting_id=id).all()
       return downvote

   def __repr__(self):
       return f'{self.id_user}:{self.posting_id}'


class PhotoProfile(db.Model):
   __tablename__ = 'profile_photos'

   id = db.Column(db.Integer,primary_key = True)
   pic_path = db.Column(db.String())
   user_id = db.Column(db.Integer,db.ForeignKey("users.id"))