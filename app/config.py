# import os

# basedir = os.path.abspath(os.path.dirname(__file__))


# class Config:
#     SQLALCHEMY_DATABASE_URI = "sqlite:///hrms.db"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = (
       f"mysql+pymysql://root:AzVeNRlfwNyZcUMovoFavZCMUOIWjMBL@mysql.railway.internal:3306/railway"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
