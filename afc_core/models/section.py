from afc_core.models import db, generate_uuid


class Section(db.Model):
    __tablename__ = 'section'

    id: str = db.Column(db.String(), primary_key=True, default=generate_uuid)
    count: str = db.Column(db.Integer())
    date = db.Column(db.DateTime, default=db.func.now())
    course_id = db.Column(db.String(), db.ForeignKey('course.id'))
    photo = db.Column(db.String(), default="")
    photo_result = db.Column(db.String(), default="")
    course = db.relationship('Course', backref="sections")

    def __init__(self, count, course_id):
        self.count = count
        self.course_id = course_id
