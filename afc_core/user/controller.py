import os

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from afc_core import APP_ROOT
from afc_core.models.user import User

from .repository import get_user_by_email, register_student
from .schema import user_schema
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


@user.route('/secret', methods=['GET'])
@jwt_required
def secret():
    user = get_jwt_identity()
    return jsonify(user)


@user.route('/register/student', methods=['POST'])
def register_student():
    dto = request.form
    avatar = request.files['avatar']
    existing_user = get_user_by_email(dto['email'])
    if existing_user:
        return {'message': 'Email is already taken'}, 400

    avatar_name = store_avatar(avatar)
    student = register_student(dto, avatar_name)
    return user_schema.jsonify(student)


@user.route('/register/teacher', methods=['POST'])
def register_teacher():
    return jsonify({'message': 'registering a teacher'})


@user.route('/reset/password', methods=['POST'])
def reset_password():
    return jsonify({'message': 'reset user password'})


@user.route('/profile', methods=['GET'])
def get_profile():
    return jsonify({'message': 'get current user profile'})


@user.route('/profile', methods=['PUT'])
def update_profile():
    return jsonify({'message': 'updating current user profile'})
