from sqlalchemy import Column, String

class Article(object):
    title = Column(String(100), nullable=False)
    content = Culumn(String(), nullable=False)

class Categories(object):
    pass

class Comment(object):
    pass

class User(object):
    pass
