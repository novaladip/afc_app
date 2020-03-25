import os
from flask import Blueprint, jsonify, request


from .utils import store_avatar
from .repository import register_student, get_user_by_email
from afc_core import APP_ROOT
from afc_core.models import db
from afc_core.models.user import User


user = Blueprint('user', __name__)


@user.route('/register/student', methods=['POST'])
def registerStudent():
    dto = request.form
    avatar = request.files['avatar']
    existing_user = get_user_by_email(dto['email'])
    if existing_user:
        return {'message': 'Email is already taken'}, 400

    avatar_name = store_avatar(avatar)

    register_student(db, dto, avatar_name)
    return {'message': 'success'}, 200


@user.route('/register/teacher', methods=['POST'])
def registerTeacher():
    return jsonify({'message': 'registering a teacher'})


@user.route('/reset/password', methods=['POST'])
def resetPassword():
    return jsonify({'message': 'reset user password'})


@user.route('/profile', methods=['GET'])
def getProfile():
    return jsonify({'message': 'get current user profile'})


@user.route('/profile', methods=['PUT'])
def updateProfile():
    return jsonify({'message': 'updating current user profile'})
