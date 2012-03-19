import datetime

from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from database import SQLAlchemy
from tornado.options import options
from pdb import set_trace as st


db = SQLAlchemy("mysql://{user}:{password}@{host}:{port}/{db}".format(
        user = options.mysql_user,
        password = options.mysql_password,
        host = options.mysql_host,
        port = options.mysql_port,
        db = options.mysql_database
    ), pool_recycle = options.mysql_pool_recycle)

class Article(db.Model):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", primaryjoin=('User.id==Article.user_id'))
    comment_totals = Column(Integer, default=0)
    tag = Column(String(250), default='')
    cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", primaryjoin=('Category.id==Article.cat_id'))
    create_time = Column(DateTime, default=datetime.datetime.now())
    update_time = Column(DateTime, onupdate=datetime.datetime.now())

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)

class Comment(db.Model):
    __tablename__ = 'comment'

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
