from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static/',
    static_path='/static'
)

app.wsgi_app = ProxyFix(app.wsgi_app)
