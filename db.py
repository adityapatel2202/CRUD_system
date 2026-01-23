import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("mysql.railway.internal"),
        user=os.environ.get("root"),
        password=os.environ.get("nHfzJIoMltcpBaBcKtygekyrVHzLQBuT"),
        database=os.environ.get("railway"),
        port=os.environ.get("3306")
    )
