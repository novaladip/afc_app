from afc_core.models import db, generate_uuid
import datetime as dt


class Course(db.Model):
    __tablename__ = 'course'

    id: str = db.Column(db.String(), primary_key=True, default=generate_uuid)
    name: str = db.Column(db.String(400), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    close_date = db.Column(db.DateTime, nullable=False)
    teacher_id = db.Column(db.String(), db.ForeignKey('user.id'))
    teacher = db.relationship('User')

    def __init__(self, name, close_date, teacher_id):
        self.name = name
        self.close_date = dt.datetime.strptime(close_date, '%Y-%m-%d')
        self.teacher_id = teacher_id
