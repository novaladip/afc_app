from flask import Blueprint, jsonify,  request

from .repository import AttendanceRepository

from afc_core.models.attendance import Attendance

attendance = Blueprint('attendance', __name__)


def update():
    pass
