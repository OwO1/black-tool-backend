# -*- coding: utf-8 -*-
import json
from json import JSONDecodeError
from flask import g
from flask import request
from apps.config import const
from apps.utils import base64_util


def parse_current_request_data():
    uid = int(request.headers.get(const.REQ_HEADER_KEY_UID, 0))
    token = str(request.headers.get(const.REQ_HEADER_KEY_TOKEN, ''))
    user = str(request.headers.get(const.REQ_HEADER_KEY_USER, '{}'))

    g.uid = uid
    g.token = token

    # 兼容 user 数据 base64 格式
    try:
        g.user = json.loads(user)
    except JSONDecodeError:
        g.user = json.loads(base64_util.decode(user))


def set_response_headers(response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers["Access-Control-Allow-Methods"] = 'POST'
    response.headers["Access-Control-Allow-Headers"] = "x-requested-with,content-type"
    return response


# 请求到达 handler 方法前调用
before_request_funcs = [
    parse_current_request_data
]

# 请求在 handler 方法处理后，响应前调用
after_request_funcs = [
    set_response_headers
]
