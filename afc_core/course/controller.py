from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity

from afc_core.middleware.auth import teacher_only

from .schema import course_schema
from .repository import create_course

course = Blueprint('course', __name__)


@course.route('/', methods=['POST'])
@teacher_only
def create():
    dto = request.form
    teacher_id = get_jwt_identity()['id']
    course = create_course(teacher_id, dto)
    return course_schema.jsonify(course), 201
