# coding:utf-8

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)

class Config(object):
    """配置参数"""
    # sqlalchemy配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://hadoop:hadoop@127.0.0.1:3306/test"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "ASEAEASGWEFEsea"

app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
pymysql.install_as_MySQLdb() 
db = SQLAlchemy(app)

# 创建数据库模型类
class Author(db.Model):
    """用户表"""
    __tablename__ = "tbl_authors" # 指明数据库的表名
    
    id = db.Column(db.Integer, primary_key=True) # 整形的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    books = db.relationship("Book", backref="author")  # 从模型类考虑

    

class Book(db.Model):
    """用户角色/身份表"""
    __tablename__ = "tbl_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


class AuthorBookForm(FlaskForm):
    """作者数据表单模型类"""
    author_name = StringField(label=u"作者",validators=[DataRequired("作者必填")] )
    book_name = StringField(label=u"书籍",validators=[DataRequired("书籍必填")] )
    submit = SubmitField(label=u"保存")



@app.route("/", methods=["GET", "POST"])
def index():
    #创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data 
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit

    # 查询数据库
    author_li = Author.query.all()
    return render_template("author_book.html", authors = author_li, form = form)



if __name__ == '__main__':
    app.run(debug=True)
