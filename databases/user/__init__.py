from app import db
from typing import Dict
from core import exist_in_this_model, make_password, verify_password
from flask_jwt_extended import create_access_token
from core import ResponseStatus


class UserResult:
    def __init__(self, data: Dict, response_status: ResponseStatus = ResponseStatus.Success):
        self.response_status: ResponseStatus = response_status
        self.data: Dict = data


class User(db.Model):
    __tablename__: str = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(100))
    password_key = db.Column(db.String(100))

    def get(self) -> Dict:
        return {
            "id": self.id,
            "fullname": self.fullname,
            "username": self.username
        }

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def register(self) -> UserResult:
        exist = exist_in_this_model(User, 'username', self.username)
        if exist:
            return UserResult(
                response_status=ResponseStatus.DataExist,
                data={
                    'message': 'already exist',
                    'field': 'username',
                    'value': self.username
                }
            )
        pw = make_password(self.password)
        self.password = pw.password
        self.password_key = pw.password_key
        try:
            self.commit()
            token = create_access_token(identity=self.id)
            return UserResult(
                data={
                    "message": "success",
                    "username": self.username,
                    "token": token
                }
            )
        except:
            return UserResult(
                response_status=ResponseStatus.SystemError,
                data={
                    'message': 'system has been crash, report this issue'
                }
            )

    def login(self) -> UserResult:
        user: User = User.query.filter_by(username=self.username).first()

        def not_found() -> UserResult:
            return UserResult(
                response_status=ResponseStatus.BadAuth,
                data={
                    "message": "username not found or password not match"
                }
            )

        if not user:
            return not_found()
        if not verify_password(user.password_key, user.password, self.password):
            return not_found()
        token = create_access_token(identity=user.id)
        return UserResult(
            data={
                "message": "logged",
                "username": self.username,
                "token": token
            }
        )
