from afc_core.models import db, generate_uuid


class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.String(), primary_key=True, default=generate_uuid)
    student_id = db.Column(db.String(), db.ForeignKey('user.id'))
    section_id = db.Column(db.String(), db.ForeignKey('section.id'))
    status: str = db.Column(db.String, default="")
    section = db.relationship('Section', backref='attendances')
    student = db.relationship('User')

    def __init__(self, student_id: str, section_id: str):
        self.student_id = student_id
        self.section_id = section_id
