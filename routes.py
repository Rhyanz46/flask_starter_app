def load_routes(app):
    from modules.user import UserRegisterHandler, UserLoginHandler

    # user
    app.add_url_rule('/user/register', view_func=UserRegisterHandler.as_view('user_register'))
    app.add_url_rule('/user/login', view_func=UserLoginHandler.as_view('user_login'))
