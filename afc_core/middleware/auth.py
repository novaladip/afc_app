from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_current_user, verify_jwt_in_request, get_jwt_identity

from afc_core.api.user.repository import get_user_by_id


def auth_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        jwt_payload = get_jwt_identity()
        user = get_user_by_id(jwt_payload['id'])
        if user is None:
            return jsonify({'message': 'Unauthorized'}), 401

        return fn(*args, **kwargs)

    return wrapper


def student_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        jwt_payload = get_jwt_identity()
        user = get_user_by_id(jwt_payload['id'])
        if user is None:
            return jsonify({'message': 'Unauthorized'}), 401

        if user.role != 'STUDENT':
            return jsonify({'message': 'Unauthorized'}), 401

        return fn(*args, **kwargs)
    return wrapper


def teacher_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        jwt_payload = get_jwt_identity()
        user = get_user_by_id(jwt_payload['id'])
        if user is None:
            return jsonify({'message': 'Unauthorized'}), 401

        if user.role != 'TEACHER':
            return jsonify({'message': 'Unauthorized'}), 401

        return fn(*args, **kwargs)
    return wrapper
