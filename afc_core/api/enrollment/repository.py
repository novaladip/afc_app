from typing import List

from afc_core.models import db
from afc_core.models.enrollment import Enrollment


def create_enrollment(student_id, course_id):
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    return enrollment


def get_all_enrollment(student_id: str):
    enrollments = Enrollment.query.filter(
        Enrollment.student_id == student_id).order_by(Enrollment.enroll_date.desc())
    return enrollments
