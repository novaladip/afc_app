from typing import List

from afc_core.models import db
from afc_core.models.section import Section
from afc_core.models.attendance import Attendance
from afc_core.api.course.repository import get_course_by_id
from afc_core.api.attendance.repository import AttendanceRepository


def create_section(course_id: str, count: int) -> Section:
    section = Section(course_id=course_id, count=count)
    course = get_course_by_id(course_id)

    db.session.add(section)
    db.session.commit()
    attendances = []
    for item in course.students:
        attendances.append(Attendance(item.student_id, section.id))

    AttendanceRepository.bulk_insert(attendances)

    return section


def get_section_by_id(section_id: str) -> Section:
    section = Section.query.filter(Section.id == section_id).first()
    return section


def get_section_by_course_id(course_id: str) -> List[Section]:
    sections = Section.query.filter(
        Section.course_id == course_id).order_by(Section.count.asc()).all()
    return sections
