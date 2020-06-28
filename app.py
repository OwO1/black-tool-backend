# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes import bp_list
from middlewares import before_request_funcs, after_request_funcs
from apps.db import db, SQLALCHEMY_DATABASE_URI

app = Flask('tools')

# SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

CORS(app, resources=r'/*')

# config before and after request functions
pb_before_request_funcs_map = {}
pb_after_request_funcs_map = {}
for bp in bp_list:
    pb_before_request_funcs_map[bp.name] = before_request_funcs
    pb_after_request_funcs_map[bp.name] = after_request_funcs
app.before_request_funcs = pb_before_request_funcs_map
app.after_request_funcs = pb_after_request_funcs_map

# register all blueprints
for bp in bp_list:
    app.register_blueprint(bp)

import commands
