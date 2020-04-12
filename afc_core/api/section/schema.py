from afc_core.manage import ma
from afc_core.api.course.schema import CourseSchema
from afc_core.api.user.schema import UserProfileSchema


class AttendancesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'student', 'status')

    student = ma.Nested(UserProfileSchema)


class SectionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'count', 'date', 'course_id',
                  'photo', 'course', 'attendances', 'links')

    course = ma.Nested(CourseSchema)
    attendances = ma.Nested(AttendancesSchema, many=True)
    links = ma.Hyperlinks({
        "class_photo": ma.URLFor("section.photo", name="<photo>")
    })


# Init schema
section_schema = SectionSchema()
sections_schema = SectionSchema(many=True)
