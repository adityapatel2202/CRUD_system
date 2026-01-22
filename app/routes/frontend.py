from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Employee
from app import db
from datetime import datetime

frontend_bp = Blueprint("frontend", __name__)


@frontend_bp.route("/")
def employees():
    employees = Employee.query.all()
    return render_template("employees.html", employees=employees)


@frontend_bp.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        visa_expiry = request.form.get("visa_expiry")

        emp = Employee(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            role=request.form.get("role"),
            visa_status=request.form.get("visa_status"),
            visa_expiry=datetime.strptime(visa_expiry, "%Y-%m-%d").date()
            if visa_expiry else None
        )

        db.session.add(emp)
        db.session.commit()
        return redirect(url_for("frontend.employees"))

    return render_template("add_employee.html")


@frontend_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):
    emp = Employee.query.get_or_404(id)

    if request.method == "POST":
        visa_expiry = request.form.get("visa_expiry")

        emp.first_name = request.form["first_name"]
        emp.last_name = request.form["last_name"]
        emp.email = request.form["email"]
        emp.role = request.form.get("role")
        emp.visa_status = request.form.get("visa_status")
        emp.visa_expiry = (
            datetime.strptime(visa_expiry, "%Y-%m-%d").date()
            if visa_expiry else None
        )

        db.session.commit()
        return redirect(url_for("frontend.employees"))

    return render_template("edit_employee.html", employee=emp)
