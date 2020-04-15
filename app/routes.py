# -*- coding: utf-8 -*-
import sys   #reload()之前必须要引入模块
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import render_template,flash,redirect,url_for,request
from werkzeug.urls import url_parse
from app import app,db
from app.forms import LoginForm,RegistrationForm,ArticleForm
from flask_login import login_required,current_user,login_user,logout_user
from app.models import User,Article
import time
#...
#import requests
#import re
#url = 'https://www.hqu.edu.cn/hdxw.htm'
#response = requests.get(url)
#response.encoding ='utf-8'
#html = response.text
#content = re.findall(r'<tr id="line_u15_0">.*?<span id="section_u15_24" style="display:none;">',html,re.S)[0]
#content2_url= re.findall(r'href="(.*?)" ',content,re.S)
#content_title=re.findall(r'<font color="">(.*?)<',content,re.S)
#post=[]
#a=0
#for content2_url in content2_url:
#     post.append({'url':'https://www.hqu.edu.cn/%s' % content2_url,'title':content_title[a]})
#     a=a+1
#...    
@app.route('/')
@app.route('/index')
#@login_required#登陆后才能访问首页
def index():
        u = User.query.get(3)
	article = u.articles.all()
	article = article[::-1]
	return render_template('index.html',articles=article)
@app.route('/login',methods=['GET','POST'])
def login():
	#判断是否登录
	if current_user.is_authenticated:
        	return redirect(url_for('index'))

	form = LoginForm()
	#对数据表格进行验证
	if form.validate_on_submit():
	#查询：查到返回User,or None
		user = User.query.filter_by(username=form.username.data).first()
        	if user is None or not user.check_password(form.password.data):
			flash('用户名或密码错误')
			return redirect(url_for('login'))#重新定位到登录页面
		login_user(user,remember=form.remember_me.data)
		next_page = request.args.get('next')#获取跳转地址
		if not next_page or url_parse(next_page).netloc !='':
			next_page = url_for('index')
			#主页
#		flash('用户登录的名户名是:{} , 是否记住我:{}'.format( form.username.data,form.remember_me.data))
       		#重定向至首页
       		return redirect(next_page)
	return render_template('login.html',title='登录',form=form)
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # 判断当前用户是否验证，如果通过的话返回首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你成为我们网站的新用户!')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)
@app.route('/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	posts = [
        {'author':user,'body':'测试Post #1号'},
        {'author':user,'body':'测试Post #2号'}]

	return render_template('user.html',user=user,posts=posts)
@app.route('/article',methods=['GET','POST'])
def article():
	form=ArticleForm()
	t=time.strftime('%Y.%m.%d.%A.%H:%M:%S',time.localtime(time.time()))
	if form.validate_on_submit():
		article = Article(head=form.head.data,title=form.title.data,body=form.body.data,author=current_user,time=t)
		db.session.add(article)
        	db.session.commit()
        	flash('你的提交已变更.')
        	return redirect(url_for('index'))
 	return render_template('article.html',form=form)

@app.route('/article_all/<article>')
def article_all(article):
	article=Article.query.get(article)
	return render_template('article_all.html',article=article)
