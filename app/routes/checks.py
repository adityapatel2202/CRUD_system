from flask import Blueprint, jsonify
from datetime import date
from app.models import Employee

checks_bp = Blueprint("checks", __name__)

@checks_bp.route("/visa/<int:emp_id>", methods=["GET"])
def visa_check(emp_id):
    emp = Employee.query.get(emp_id)

    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    if not emp.visa_expiry:
        return jsonify({
            "visa_status": "No visa required",
            "visa_expiry": "N/A"
        })

    status = "Visa Valid" if emp.visa_expiry >= date.today() else "Visa Expired"

    return jsonify({
        "visa_status": status,
        "visa_expiry": emp.visa_expiry.strftime("%Y-%m-%d")
    })
