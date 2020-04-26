from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from configurations import set_config
from databases import load_db
from routes import load_routes

app = Flask(__name__)
set_config(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
mg = Migrate(app, db)
cors = CORS(app)
load_db()
load_routes(app)

if __name__ == '__main__':
    app.run()
