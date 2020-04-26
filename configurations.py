from os import getenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class Database:
    def __init__(self):
        self.user = getenv("DATABASE_USER")
        self.host = getenv("DATABASE_HOST")
        self.name = getenv("DATABASE_NAME")
        self.password = getenv("DATABASE_PASSWORD")
        self.port = getenv("DATABASE_PORT")


def set_config(app) -> None:
    db = Database()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db.user}:{db.password}@{db.host}/{db.name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['JWT_SECRET_KEY'] = "dedadewa"
