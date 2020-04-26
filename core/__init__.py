from cryptography.fernet import Fernet
from app import db
from enum import Enum
from collections import namedtuple

res = namedtuple('response_value', 'id, res_code')


class ResponseStatus(Enum):
    Success = res(0, 200)
    Created = res(1, 201)
    DataExist = res(2, 400)
    BadRequest = res(3, 400)
    SystemError = res(4, 500)
    BadAuth = res(5, 403)


class Out:
    def __init__(self):
        self.password = None
        self.password_key = None


def exist_in_this_model(model: db.Model, model_field: str, value):
    if hasattr(model, model_field):
        obj_model = getattr(getattr(model, 'query'), 'filter')(getattr(model, model_field) == value).first()
        if obj_model:
            return obj_model
    return False


def make_password(text_plain: str) -> Out:
    key = Fernet.generate_key()
    f = Fernet(key)
    out = Out()
    out.password_key = key.decode()
    out.password = f.encrypt(str.encode(text_plain)).decode()
    return out


def verify_password(password_key: str, password: str, plain_text: str) -> bool:
    f = Fernet(str.encode(password_key))
    token = f.encrypt(str.encode(plain_text))
    if f.decrypt(str.encode(password)).decode() == f.decrypt(token).decode():
        return True
    return False
