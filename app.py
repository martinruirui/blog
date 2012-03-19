import sys
import os
import tornado.web
import tornado.database
import tornado.httpserver
import tornado.ioloop

from pdb import set_trace as st
from tornado.options import define

import yaml

configs = yaml.load(open("config.yaml"))

define("mysql_port", default=int(configs['db']['port']), help="connect database use this port", type=int)
define("mysql_host", default=configs['db']['host'], help="blog database host")
define("mysql_database", default=configs['db']['database'], help="blog database name")
define("mysql_user", default=configs['db']['user'], help="blog database user")
define("mysql_password", default=configs['db']['password'], help="blog database password")
define("mysql_pool_recycle", default=int(configs['db']['pool_recycle']), help="blog database pool recycle", type=int)

tornado.options.parse_command_line()

APP_DIR = os.path.abspath(os.path.dirname(__file__))

PROJECT_DIR = os.path.dirname(APP_DIR)
NAMESPACE = os.path.basename(APP_DIR)

BLOG_DIR = os.path.join(APP_DIR, "blog")

# join path
APP_DIR in sys.path or sys.path.append(APP_DIR)
BLOG_DIR in sys.path or sys.path.append(BLOG_DIR)
PROJECT_DIR in sys.path or sys.path.append(PROJECT_DIR)

for root, dirs, files in os.walk(BLOG_DIR):
    root in sys.path or sys.path.append(root)
import urls

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
                blog_title = configs['blog_title'],
                template_path = configs['template_path'],
                static_path = configs['static_path'],
                xsrf_cookies = configs['xsrf'],
                cookie_secret = configs['cookie_secret'],
                login_url = configs['login_url'],
                autoescape = configs['autoescape'],
        )
        tornado.web.Application.__init__(self, urls.urlpatterns, **settings)

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(configs['server']['port'])
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
