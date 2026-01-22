import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.environ.get('MYSQLUSER')}:"
        f"{os.environ.get('MYSQLPASSWORD')}@"
        f"{os.environ.get('MYSQLHOST')}:"
        f"{os.environ.get('MYSQLPORT')}/"
        f"{os.environ.get('MYSQLDATABASE')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
