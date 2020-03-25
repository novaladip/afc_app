import bcrypt
import os
import calendar
import time
from flask import current_app
from flask_jwt_extended import create_access_token
from werkzeug.utils import secure_filename


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)).decode()


def compare_password(hashed_password: str, password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def store_avatar(file) -> str:
    timestamp = calendar.timegm(time.gmtime())
    filename = f'{timestamp}_{secure_filename(file.filename)}'
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    return filename


def create_bearer_token(user):
    return create_access_token(identity={'id': user.id, 'email': user.email, 'role': user.role})
