import bcrypt
import os
import calendar
import time
import math
from datetime import timedelta
from flask import current_app
from flask_jwt_extended import create_access_token
from werkzeug.utils import secure_filename
from PIL import Image


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)).decode()


def compare_password(hashed_password: str, password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def store_avatar(file) -> str:
    timestamp = calendar.timegm(time.gmtime())
    filename = f'{timestamp}_{secure_filename(file.filename)}'
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    filesize = os.stat(filepath).st_size / 1000

    if (filesize > 100):
        avatar = Image.open(filepath)
        x, y = avatar.size
        x2, y2 = math.floor(x / 2), math.floor(y / 2)
        avatar = avatar.resize((x2, y2), Image.ANTIALIAS)
        avatar.save(filepath)
        return filename

    return filename


def create_bearer_token(user):
    expires = timedelta(days=30)
    return create_access_token(identity={'id': user.id, 'email': user.email, 'role': user.role}, expires_delta=expires)
