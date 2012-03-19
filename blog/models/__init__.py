#encoding = utf-8
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime, Text
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
    title = Column('title', String(100), nullable=False)
    content = Column('content', Text(), nullable=False, default=u'')
    user_id = Column('user_id', Integer, ForeignKey('user.id'), default=0)
    comment_totals = Column('comment_totals', Integer, default=0)
    tag = Column('tag', String(250), default=None)
    cat_id = Column('cat_id', Integer, ForeignKey('category.id'), default=0)
    create_time = Column('create_time', DateTime, default=datetime.datetime.now())
    update_time = Column('update_time', DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)

class Comment(db.Model):
    __tablename__ = 'comment'

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
