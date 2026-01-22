import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from app import create_app
from app.models import db, Employee

# Create a fresh app + DB for each test module
def setup_module(module):
    global app, client
    app = create_app(testing=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.create_all()

    client = app.test_client()


# ---------- TEST: CREATE EMPLOYEE ----------
def test_create_employee():
    payload = {
        "first_name": "Alice",
        "last_name": "Brown",
        "email": "alice_create@example.com",    # UNIQUE
        "role": "HR Assistant"
    }

    res = client.post("/api/employees/", json=payload)
    assert res.status_code == 201
    data = res.get_json()
    assert data["first_name"] == "Alice"


# ---------- TEST: GET EMPLOYEES ----------
def test_get_employees():
    res = client.get("/api/employees/")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)


# ---------- TEST: UPDATE EMPLOYEE ----------
def test_update_employee():
    emp = Employee(
        first_name="Test",
        last_name="User",
        email="unique_update@example.com",      # UNIQUE
        role="Tester"
    )
    with app.app_context():
        db.session.add(emp)
        db.session.commit()
        emp_id = emp.id

    res = client.put(f"/api/employees/{emp_id}", json={"role": "Senior Tester"})
    assert res.status_code == 200
    assert res.get_json()["role"] == "Senior Tester"


# ---------- TEST: DELETE EMPLOYEE ----------
def test_delete_employee():
    emp = Employee(
        first_name="Delete",
        last_name="Me",
        email="unique_delete@example.com",      # UNIQUE
        role="Temp"
    )
    with app.app_context():
        db.session.add(emp)
        db.session.commit()
        emp_id = emp.id

    res = client.delete(f"/api/employees/{emp_id}")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Employee deleted"


# # ---------- TEST: DBS CHECK ----------
# def test_dbs_check():
#     res = client.post("/api/checks/dbs", json={"name": "John Doe"})
#     assert res.status_code == 200
#     assert res.get_json()["dbs_status"] == "Clear"


# # ---------- TEST: CREDIT CHECK ----------
# def test_credit_check():
#     res = client.post("/api/checks/credit", json={"name": "John Doe"})
#     assert res.status_code == 200
#     assert res.get_json()["credit_status"] == "Good"


# # ---------- TEST: RIGHT-TO-WORK CHECK ----------
# def test_rtw_check():
#     res = client.post("/api/checks/right-to-work", json={"name": "John Doe"})
#     assert res.status_code == 200
#     assert "Eligible" in res.get_json()["rtw_status"]
