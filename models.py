# -*- coding: utf-8 -*-
from datetime import datetime
from app import db

class Commands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(200))
    command = db.Column(db.String(200))
    introduce = db.Column(db.String(200))


# class User(db.Model):
#     #  账号表
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20))
#     username = db.Column(db.String(20))
#     # 存储加密后的密码
#     password = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     create_time = db.Column(db.DateTime, default=datetime.utcnow)


# class UserInfo(db.Model):
#     #  用户记录表
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     # 积分
#     point = db.Column(db.Integer)
#     # 能量
#     energy = db.Column(db.Integer)
#     # 关卡
#     level = db.Column(db.Integer)
#     create_time = db.Column(db.DateTime, default=datetime.utcnow)


# class History(db.Model):
#     # 历史的游戏数据
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     point = db.Column(db.Integer)
#     create_time = db.Column(db.DateTime, default=datetime.utcnow)


# class Friendship(db.Model):
#     #  好友表
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     friend_id = db.Column(db.Integer)
#     create_time = db.Column(db.DateTime, default=datetime.utcnow)


# class RankingList(db.Model):
#     #  排行榜
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     level = db.Column(db.Integer)
#     point = db.Column(db.Integer)
#     create_time = db.Column(db.DateTime, default=datetime.utcnow)


# class UserSecurityCode(db.Model):
#     #  存储验证码
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     security_code = db.Column(db.String(100))
#     create_time = db.Column(db.DateTime, default=datetime.utcnow)
#     # 1为使用 0为未使用
#     status = db.Column(db.Integer)
