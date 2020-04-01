import os

from flask import Blueprint, jsonify, request, current_app, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from afc_core import APP_ROOT
from afc_core.models.user import User
from afc_core.middleware.auth import auth_required

from .repository import get_user_by_email, get_user_by_id, register_student, register_teacher, update_user_profile
from .schema import user_schema, user_profile_schema
from .utils import store_avatar, compare_password, hash_password, create_bearer_token

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def sign_in():
    dto = request.form
    user = get_user_by_email(dto['email'])

    if user is None:
        return jsonify({'message': 'User not found'}), 400

    if compare_password(user.password, dto['password']) == False:
        return jsonify({'message': 'Invalid password'}), 400

    bearer_token = create_bearer_token(user)

    return jsonify(bearer_token=bearer_token)


@user.route('/register/student', methods=['POST'])
def sign_up_student():
    dto = request.form
    avatar = request.files['avatar']
    existing_user = get_user_by_email(dto['email'])
    if existing_user:
        return {'message': 'Email is already taken'}, 400

    avatar_name = store_avatar(avatar)
    student = register_student(dto, avatar_name)
    return user_schema.jsonify(student)


@user.route('/register/teacher', methods=['POST'])
def sign_up_teacher():
    dto = request.form
    avatar = request.files['avatar']
    existing_user = get_user_by_email(dto['email'])
    if existing_user:
        return jsonify({'message': 'Email is already taken'}), 400

    avatar_name = store_avatar(avatar)
    teacher = register_teacher(dto, avatar_name)

    return user_schema.jsonify(teacher), 201


@user.route('/reset/password', methods=['POST'])
def reset_password():
    return jsonify({'message': 'reset user password'})


@user.route('/profile', methods=['GET'])
@auth_required
def get_profile():
    jwt_payload = get_jwt_identity()
    user = get_user_by_id(jwt_payload['id'])
    return user_profile_schema.jsonify(user)


@user.route('/profile', methods=['PUT'])
@auth_required
def update_profile():
    avatar = request.files['avatar']
    avatar_name = store_avatar(avatar)
    user_id = get_jwt_identity()['id']
    updated_user = update_user_profile(user_id, avatar_name)
    return user_profile_schema.jsonify(updated_user)


@user.route('/avatar/<name>', methods=['GET'])
def show_avatar(name):
    avatar_dir = os.path.join(current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(avatar_dir, name)
