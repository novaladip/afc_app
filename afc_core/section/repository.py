from typing import List

from afc_core.models import db
from afc_core.models.section import Section


def create_section(course_id: str, count: int) -> Section:
    section = Section(course_id=course_id, count=count)
    db.session.add(section)
    db.session.commit()
    return section


def get_section_by_id(section_id: str) -> Section:
    section = Section.query.filter(Section.id == section_id).first()
    return section


def get_section_by_course_id(course_id: str) -> List[Section]:
    sections = Section.query.filter(
        Section.course_id == course_id).order_by(Section.count.asc()).all()
    return sections
