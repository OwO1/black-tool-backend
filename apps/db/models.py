# -*- coding: utf-8 -*-
import datetime
import enum

from ..db import db
from enums import TodoStatusEnum, TodoTypeEnum, DeletedStatusEnum


# class BaseModel(db.Model):
#     __abstract__ = True

#     id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment="自增id")
#     create_time = db.Column(db.DateTime, index=True, nullable=False, server_default=db.text('NOW()'), comment="创建时间")
#     update_time = db.Column(db.DateTime, index=True, nullable=False, server_default=db.text('NOW()'), onupdate=datetime.datetime.now, comment="更新时间")
#     delete_time = db.Column(db.DateTime, index=True, nullable=True, comment="删除时间")


class Commands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(200))
    command = db.Column(db.String(200))
    introduce = db.Column(db.String(200))
    deleted = db.Column(db.Integer, nullable=False, default=str(DeletedStatusEnum.EXIST.value), server_default=str(DeletedStatusEnum.EXIST.value), comment='是否被删除')


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200), nullable=False, default='', server_default='', comment='代办事项')
    note = db.Column(db.String(200), nullable=True, comment='代办事项备注')
    status = db.Column(db.Integer, nullable=False, default=str(TodoStatusEnum.UNFINISHED.value), server_default=str(TodoStatusEnum.UNFINISHED.value), comment='代办事项完成状态')
    todo_type = db.Column(db.Integer, nullable=False, default=str(TodoTypeEnum.TODAY.value), server_default=str(TodoTypeEnum.TODAY.value), comment='代办事项类型')
    deleted = db.Column(db.Integer, nullable=False, default=str(DeletedStatusEnum.EXIST.value), server_default=str(DeletedStatusEnum.EXIST.value), comment='是否被删除')
