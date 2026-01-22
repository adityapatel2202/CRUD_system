# app/models.py
from app import db
from datetime import date

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    role = db.Column(db.String(100))

    visa_status = db.Column(db.String(50))        # e.g. Valid / Expired
    visa_expiry = db.Column(db.Date)              # expiry date
