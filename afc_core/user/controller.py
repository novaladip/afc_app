from flask import Blueprint, jsonify, request

from afc_core.models.user import User

user = Blueprint('user', __name__)


@user.route('/register/student', methods=['POST'])
def registerStudent():
    return jsonify({'message': 'registering a student'})


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
