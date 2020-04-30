from flask import Blueprint, jsonify,  request

from .repository import AttendanceRepository

from afc_core.models.attendance import Attendance
from afc_core.middleware.auth import teacher_only

attendance = Blueprint('attendance', __name__)


@teacher_only
@attendance.route('/update/bulk', methods=['PUT'])
def update():
    data = request.json
    AttendanceRepository.bulk_update(data)
    return data
