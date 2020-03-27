from flask import Blueprint, jsonify, request

from .schema import section_schema,  sections_schema
from .repository import get_section_by_course_id, get_section_by_id, create_section

from afc_core.middleware.auth import auth_required, teacher_only


section = Blueprint('section', __name__)


@section.route('/course/<course_id>', methods=['GET'])
@auth_required
def get_section(course_id: str):
    sections = get_section_by_course_id(course_id)
    result = sections_schema.dump(sections)
    return jsonify(result)


@section.route('/', methods=['POST'])
@teacher_only
def add_section():
    form = request.form
    section = create_section(form['course_id'], form['count'])
    return section_schema.jsonify(section)


@section.route('/<section_id>', methods=['GET'])
@teacher_only
def get_detail_section(section_id: str):
    section = get_section_by_id(section_id)
    return section_schema.jsonify(section)
