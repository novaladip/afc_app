import bcrypt
import os
import calendar
import time
from flask import current_app
from werkzeug.utils import secure_filename


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password, bcrypt.gensalt(12)).decode()


def compare_password(hashed_password: str, password: str) -> bool:
    return hashed_password == hash_password(password)


def store_avatar(file) -> str:
    timestamp = calendar.timegm(time.gmtime())
    filename = f'{timestamp}_{secure_filename(file.filename)}'
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    return filename
