from typing import List

from afc_core.models import db
from afc_core.models.attendance import Attendance


class AttendanceRepository:
    @staticmethod
    def create(section_id: str, student_id: str) -> Attendance:
        attendance = Attendance(student_id=student_id, section_id=section_id)
        db.session.add(attendance)
        db.session.commit()
        return attendance

    @staticmethod
    def bulk_insert(attendances: List[Attendance]) -> List[Attendance]:
        db.session.bulk_save_objects(attendances)
        db.session.commit()
        return attendances

    @staticmethod
    def bulk_update(data):
        for a in data['attendances']:
            Attendance.query.filter(Attendance.id == a['id']).update(
                {Attendance.status: a['status']})

        db.session.commit()
