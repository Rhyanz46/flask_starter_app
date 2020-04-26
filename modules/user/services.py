from flask import Response
from typing import Dict
from json import dumps

from databases.user import User, UserResult


def register(data: Dict):
    user: User = User(
        username=data['username'],
        fullname=data['fullname'],
        password=data['password']
    )
    res: UserResult = user.register()
    return Response(
        dumps(res.data),
        status=res.response_status.value.res_code,
        mimetype='application/json'
    )


def login(data: Dict):
    user: User = User(username=data['username'], password=data['password'])
    res: UserResult = user.login()
    return Response(
        dumps(res.data),
        status=res.response_status.value.res_code,
        mimetype='application/json'
    )
