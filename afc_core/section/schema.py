from afc_core.manage import ma
from afc_core.course.schema import CourseSchema


class SectionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'count', 'date', 'course_id', 'photo', 'course')

    course = ma.Nested(CourseSchema)


# Init schema
section_schema = SectionSchema()
sections_schema = SectionSchema(many=True)
