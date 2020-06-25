# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template, jsonify, request
from models import *
from app import app, db
# from flask_cors import CORS


@app.route('/home/', methods=['GET'])
def home():
    print('1111111')
    data = [
        {
            'about': 'docker',
            'command': 'docker init 333',
            'introduce': '初始化'
        },
    ]
    res = {
        "status": 200,
        "data": data,
        "msg": "ok",
    }
    return jsonify(res)
