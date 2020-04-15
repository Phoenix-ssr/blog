#-*- encoding:utf-8 -*-
from flask_login import UserMixin
from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',backref='author',lazy='dynamic')
    articles = db.relationship('Article',backref='author',lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<用户名：{}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Article(db.Model):
	__tablename__='article'
	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.String(4000))
	head = db.Column(db.String(30))
	title= db.Column(db.String(20))
	time = db.Column(db.String(20))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	def __repr__(self):
        	return '{}'.format(self.id)

