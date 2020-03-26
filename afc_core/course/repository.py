from flask_sqlalchemy import SQLAlchemy

from afc_core.models import db
from afc_core.models.course import Course


def get_courses():
    courses = Course.query.all()
    return courses


def create_course(teacher_id, form) -> Course:
    course = Course(name=form['name'],
                    close_date=form['close_date'], teacher_id=teacher_id)
    db.session.add(course)
    db.session.commit()
    return course
