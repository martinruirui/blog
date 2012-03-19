from blog.handlers import HomeHandler, ArticleHandler, CategoryHandler, \
        CommentHandler, AuthLoginHandler, AuthLogoutHandler

urlpatterns = [
    (r'/', HomeHandler),
    (r'/article', ArticleHandler),
    (r'/article/(?P<id>\d+)', ArticleHandler),
    (r'/categories', CategoryHandler),
    (r'/comment/(?P<article_id>\d+)', CommentHandler),
    (r'/auth/login', AuthLoginHandler),
    (r'/auth/logout', AuthLogoutHandler),
]
