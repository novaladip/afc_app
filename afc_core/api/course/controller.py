from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity

from afc_core.middleware.auth import teacher_only, auth_required

from .schema import course_schema, courses_schema, course_student_schema
from .repository import create_course, get_available_courses, get_teacher_courses, get_course_by_id

course = Blueprint('course', __name__)


@course.route('/', methods=['GET'])
@auth_required
def get():
    courses = []
    jwt_payload = get_jwt_identity()
    if jwt_payload['role'] == "STUDENT":
        courses = get_available_courses()
    else:
        courses = get_teacher_courses(jwt_payload['id'])

    result = courses_schema.dump(courses)
    return jsonify(result)


@course.route('/<course_id>', methods=['GET'])
@teacher_only
def get_by_id(course_id: str):
    course = get_course_by_id(course_id)
    return course_student_schema.jsonify(course)


@course.route('/', methods=['POST'])
@teacher_only
def create():
    dto = request.form
    teacher_id = get_jwt_identity()['id']
    course = create_course(teacher_id, dto)
    return course_schema.jsonify(course), 201
