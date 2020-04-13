import os
from flask import Blueprint, jsonify, request, current_app, send_from_directory

from .utils import store_class_photo,  Student, recognize_student_faces
from .schema import section_schema,  sections_schema, students_schema
from .repository import get_section_by_course_id, get_section_by_id, create_section, save_class_photo

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


@section.route('/<section_id>/recognize/student', methods=['POST'])
@teacher_only
def recognize_student(section_id):
    class_photo = request.files['photo']
    old_section = get_section_by_id(section_id)
    file_name = store_class_photo(class_photo)
    students = []

    for attendance in old_section.attendances:
        students.append(Student(
            attendance.student.id,
            attendance.student.last_name,
            os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                attendance.student.avatar
            ),
        ))

    [students, faces, faces_mark] = recognize_student_faces(students, os.path.join(
        current_app.config['UPLOAD_FOLDER'],
        file_name
    ),)

    new_section = save_class_photo(section_id, file_name, faces_mark)

    result = students_schema.dump(students)

    return jsonify({'result': result, 'face_founds': faces, 'face_mark': f'/api/section/photo/{faces_mark}'})


@section.route('/photo/<name>', methods=['GET'])
def photo(name):
    upload_dir = os.path.join(current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(upload_dir, name)
