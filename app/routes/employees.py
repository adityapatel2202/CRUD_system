from flask import Blueprint, request, jsonify
from app.models import db, Employee
from app.schemas import EmployeeSchema

employees_bp = Blueprint("employees", __name__)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

# CREATE Employee (Fixed)
@employees_bp.route("/", methods=["POST"])
def create_employee():
    data = request.get_json()

    emp = Employee(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        role=data.get("role")
    )

    db.session.add(emp)
    db.session.commit()

    return jsonify(employee_schema.dump(emp)), 201


# GET all employees
@employees_bp.route("/", methods=["GET"])
def get_employees():
    emps = Employee.query.all()
    return jsonify(employees_schema.dump(emps)), 200


# GET one employee
@employees_bp.route("/<int:id>", methods=["GET"])
def get_employee(id):
    emp = Employee.query.get_or_404(id)
    return jsonify(employee_schema.dump(emp)), 200


# UPDATE employee
@employees_bp.route("/<int:id>", methods=["PUT"])
def update_employee(id):
    emp = Employee.query.get_or_404(id)
    data = request.get_json()

    if "first_name" in data:
        emp.first_name = data["first_name"]
    if "last_name" in data:
        emp.last_name = data["last_name"]
    if "email" in data:
        emp.email = data["email"]
    if "role" in data:
        emp.role = data["role"]

    db.session.commit()
    return jsonify(employee_schema.dump(emp)), 200


# DELETE employee
@employees_bp.route("/<int:id>", methods=["DELETE"])
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted"}), 200
