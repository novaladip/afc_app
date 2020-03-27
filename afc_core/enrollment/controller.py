from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity

from .repository import create_enrollment, get_all_enrollment
from .schema import enrollment_schema, enrollments_schema
from afc_core.middleware.auth import student_only

enrollment = Blueprint('Enrollment', __name__)


@enrollment.route('/<course_id>', methods=['POST'])
@student_only
def enroll_course(course_id: str):
    jwt_payload = get_jwt_identity()
    enrollment_course = create_enrollment(jwt_payload['id'], course_id)

    return enrollment_schema.jsonify(enrollment_course), 201


@enrollment.route('/', methods=['GET'])
@student_only
def get_enrollments():
    jwt_payload = get_jwt_identity()
    enrollments = get_all_enrollment(jwt_payload['id'])

    result = enrollments_schema.dump(enrollments)
    return jsonify(result)
