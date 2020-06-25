# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask('tools')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources=r'/*')

import views, commands