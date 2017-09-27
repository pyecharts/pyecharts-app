from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__, static_folder='static')
bootstrap = Bootstrap(app)


from . import views
