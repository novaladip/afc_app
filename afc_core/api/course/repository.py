from flask_sqlalchemy import SQLAlchemy
import datetime as dt
from typing import List

from afc_core.models import db
from afc_core.models.user import User
from afc_core.models.course import Course


def get_available_courses() -> List[Course]:
    now = dt.datetime.utcnow()
    courses = Course.query.filter(Course.close_date > now).all()
    return courses


def get_teacher_courses(teacher_id: str) -> List[Course]:
    courses = Course.query.order_by(Course.created_at.desc()).filter(
        Course.teacher_id == teacher_id).all()
    return courses


def create_course(teacher_id, form) -> Course:
    course = Course(name=form['name'],
                    close_date=form['close_date'], teacher_id=teacher_id)
    db.session.add(course)
    db.session.commit()
    return course


def get_course_by_id(course_id: str) -> Course:
    course = Course.query.filter(Course.id == course_id).first()
    return course
