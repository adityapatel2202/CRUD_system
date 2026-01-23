# import os

# basedir = os.path.abspath(os.path.dirname(__file__))


# class Config:
#     SQLALCHEMY_DATABASE_URI = "sqlite:///hrms.db"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('root')}:{os.getenv('AzVeNRlfwNyZcUMovoFavZCMUOIWjMBL')}"
        f"@{os.getenv('mysql.railway.internal')}:{os.getenv('3306')}/{os.getenv('railway')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
