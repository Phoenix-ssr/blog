# blog
## 目录
[TOC]
### 项目地址：
>欢迎来到Phoenix的博客! http://121.199.9.81
>项目代码已上传至github: https://github.com/Phoenix-ssr/blog

### 项目结构：
```
├── app
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py
│   ├── __pycache__
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   ├── editor.md
│   │   ├── img
│   │   └── js
│   └── templates
│       ├── article_all.html
│       ├── article_base.html
│       ├── article.html
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── md_test.html
│       ├── register.html
│       ├── sun.html
│       └── user.html
├── config.py
├── dockerfile
├── gunicorn.log
├── gunicorn.sh
├── migrations
├── myblog.py
├── nohup.out
├── __pycache__
│   └── myblog.cpython-36.pyc
└── requirements.txt
```
### 前端
1. 导航

写在基础模板（base.html）中,主要是一个链表

2. 首页

继承于基础模板的index.html
![JCsO56.png](https://s1.ax1x.com/2020/04/15/JCsO56.png)

3. 文章

暂时无用的一个链接，有一个下拉菜单

4. 登录
 
继承于sun.html
![JCsjPK.png](https://s1.ax1x.com/2020/04/15/JCsjPK.png)
登陆后具有用户中心和编辑两个功能<br>
1.用户中心：
<br>想实现用户对自己的介绍，目前只有测试
<br>继承于基础模板
![JCszxe.png](https://s1.ax1x.com/2020/04/15/JCszxe.png)
2.编辑：
<br>在线md编辑功能，并且可以将内容上传数据库
<br>继承于article_base.html
![JCsv8O.png](https://s1.ax1x.com/2020/04/15/JCsv8O.png)

5. 注册
功能关闭

6. 关于我
应该是我的自我介绍，目前懒就没写了。。。。

### 后端

1. route.py
网址的路由及功能的实现
<br>下为登录功能的实现:
调用了flask_login库
![JChW5j.png](https://s1.ax1x.com/2020/04/15/JChW5j.png)
2. modle.py
数据库关系模型<br>创建数据库中的表
'''
flask db migrate -m 'users_table'
flask db upgrade
'''
![JC4oYd.png](https://s1.ax1x.com/2020/04/15/JC4oYd.png)
3. form.py
表单模型
![JC5ttH.png](https://s1.ax1x.com/2020/04/15/JC5ttH.png)

简述编辑页面的实现过程：
1. html页面中引用editor.md的css以及js文件<br>
通过form标签引用表单，设置textarea的name属性来获取编辑器内的内容
2. route.py中引用form.py的编辑表格，并写提交方法

### docker
1. 编写应用所需模块的下载文件requirements.txt
```
gunicorn==0.14.0
gevent
flask
flask-sqlalchemy
flask-migrate
pymysql
flask-wtf
flask_login
```
2. docker镜像的构建文件dockerfile
```
FROM python:2.7
WORKDIR /home/zhangwenjie/blog
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ./gunicorn.sh
```

构建容器：
```
sudo docker build -t 'blog' .
```
注意命令结尾的"点"

```
sudo docker images
```
>临时运行docker镜像：
```
sudo docker run -it --rm -p 5000:5000 blog
```
运行：
```
docker run -p 127.0.0.1:5000:80/tcp -d blog
```
查看：
```
docker ps -a
```
中止：
```
docker rm id   #若无效使用-f
```
