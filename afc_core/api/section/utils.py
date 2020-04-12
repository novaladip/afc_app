import os
import calendar
import time
from datetime import timedelta
from flask import current_app
from werkzeug.utils import secure_filename


def store_class_photo(file) -> str:
    timestamp = calendar.timegm(time.gmtime())
    filename = f'section_{timestamp}_{secure_filename(file.filename)}'
    upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_folder)
    return filename
