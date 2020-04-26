from flask.views import MethodView
from flask import request
from modules.user.services import register, login
from core.parser import ValueChecker


class UserRegisterHandler(MethodView):
    @staticmethod
    def post():
        data = ValueChecker(request.json)
        data.parse('username', str, length=20)
        data.parse('fullname', str, length=20)
        data.parse('password', str, length=20)
        return register(data.get_parsed())


class UserLoginHandler(MethodView):
    @staticmethod
    def post():
        data = ValueChecker(request.json)
        data.parse('username', str, length=20)
        data.parse('password', str, length=20)
        return login(data.get_parsed())
