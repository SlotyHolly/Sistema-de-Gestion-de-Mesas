from flask import Blueprint, jsonify, request
from models.employee import Employee, db

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([e.name for e in employees])

@employee_bp.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(name=data['name'], role=data['role'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully'})