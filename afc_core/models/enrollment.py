from afc_core.models import db, generate_uuid


class Enrollment(db.Model):
    __tablename = 'enrollment'

    id: str = db.Column(db.String(), primary_key=True, default=generate_uuid)
    enroll_date = db.Column(db.DateTime, default=db.func.now())
    student_id: str = db.Column(db.String(), db.ForeignKey('user.id'))
    course_id: str = db.Column(db.String(), db.ForeignKey('course.id'))
    student = db.relationship('User')
    course = db.relationship('Course')

    def __init__(self, student_id: str, course_id: str):
        self.student_id = student_id
        self.course_id = course_id
