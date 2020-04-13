import os
import calendar
import time
from typing import List
import face_recognition as fr
from PIL import Image, ImageDraw
from datetime import timedelta
from flask import current_app
from werkzeug.utils import secure_filename


class Student:
    is_matches = False

    def __init__(self, id, name, photo):
        self.id = id
        self.name = name
        self.photo = photo

    def update_match(self, value: bool):
        self.is_matches = value


def store_class_photo(file) -> str:
    timestamp = calendar.timegm(time.gmtime())
    filename = f'section_{timestamp}_{secure_filename(file.filename)}'
    upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_folder)
    return filename


def recognize_student_faces(students: List[Student], class_photo):
    known_faces_encodings = []
    known_faces_name = []

    for student in students:
        img = fr.load_image_file(student.photo)
        encoding = fr.face_encodings(img)[0]
        known_faces_encodings.append(encoding)
        known_faces_name.append(student.name)

    section_img = fr.load_image_file(class_photo)

    # Find faces in section photo
    face_locations = fr.face_locations(section_img)
    face_encodings = fr.face_encodings(section_img, face_locations)

    # Convert section image to pil_image
    pil_image = Image.fromarray(section_img)

    # Create a ImageDraw instance
    draw = ImageDraw.Draw(pil_image)

    # Loop known faces in section img
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(
            known_faces_encodings,
            face_encoding,
            0.45,
        )

        if True in matches:
            first_match_index = matches.index(True)
            name = known_faces_name[first_match_index]
            students[first_match_index].update_match(True)

            # Draw box
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0))

            # Draw label
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right,
                                                                bottom)), fill=(0, 255, 0), outline=(0, 255, 0))
            draw.text((left + 6, bottom - text_height - 5),
                      name, fill=(0, 0, 0))
        else:
            name = 'unknown'

            # Draw box
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))

            # Draw label
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right,
                                                                bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
            draw.text((left + 6, bottom - text_height - 5),
                      name, fill=(255, 255, 255))

    del draw
    timestamp = calendar.timegm(time.gmtime())
    file_name = f'section_result_{timestamp}.jpg'
    upload_folder = os.path.join(
        current_app.config['UPLOAD_FOLDER'], file_name)
    pil_image.save(upload_folder)
    return [students, len(face_locations), file_name]
