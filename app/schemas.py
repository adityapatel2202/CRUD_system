from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import Employee

class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True
