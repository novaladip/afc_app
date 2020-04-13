from flask import Blueprint, jsonify,  request

from .repository import AttendanceRepository

from afc_core.models.attendance import Attendance

attendance = Blueprint('attendance', __name__)


@attendance.route('/update/bulk', methods=['PUT'])
def update():
    data = request.json
    AttendanceRepository.bulk_update(data)
    return data
