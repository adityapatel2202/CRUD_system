import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///hrms.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
