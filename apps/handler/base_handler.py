from flask.views import MethodView
from flask import jsonify, request


SUCCESS_CODE = 0
SUCCESS_MSG = '成功'

HTTP_GET = 'GET'
HTTP_POST = 'POST'


class BaseHandler(MethodView):
    def __init__(self):
        self.req_form = self.get_request_form()

    @staticmethod
    def success(msg=SUCCESS_MSG, data=None):
        result = {
            'code': SUCCESS_CODE,
            'msg': msg
        }

        # 不返回数据
        if data is None:
            return jsonify(result)

        # 返回 list 数据
        if isinstance(data, list):
            result['data'] = {
                'list': data
            }
        else:
            # 返回 dict 数据
            result['data'] = data
        return jsonify(result)

    @staticmethod
    def fail(error_code, data=None):
        result = {
            'code': error_code[0],
            'msg': error_code[1]
        }

        if data:
            result['data'] = data
        return jsonify(result)

    @staticmethod
    def get_request_form():
        if request.method == HTTP_GET:
            return request.args.to_dict(flat=True)
        if request.method == HTTP_POST:
            if not request.data:
                return {}
            if not request.is_json:
                pass
            return request.get_json()
        return {}
