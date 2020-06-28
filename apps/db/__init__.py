# -*- coding: utf-8 -*-
import os
import sys
from flask_sqlalchemy import SQLAlchemy


# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

root_path = os.getcwd()
print('root_path:', root_path)
dev_db = prefix + os.path.join(root_path, 'data.db')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

db = SQLAlchemy()
session = db.session
