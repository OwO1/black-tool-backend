# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template, jsonify, request
from models import *
from app import app, db
# from flask_cors import CORS


@app.route('/home/', methods=['GET'])
def home():
    commands = Commands.query.all()
    command_list = []
    for c in commands:
        command_list.append({
            'about': c.about,
            'command': c.command,
            'introduce': c.introduce,
        })

    res = {
        "status": 200,
        "data": command_list,
        "msg": "ok",
    }
    return jsonify(res)
