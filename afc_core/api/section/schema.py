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
                  'photo', 'photo_result' 'course', 'attendances', 'links')

    course = ma.Nested(CourseSchema)
    attendances = ma.Nested(AttendancesSchema, many=True)
    links = ma.Hyperlinks({
        "class_photo": ma.URLFor("section.photo", name="<photo>"),
        "class_photo_result": ma.URLFor("section.photo", name="<photo_result>"),
    })


class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'is_matches', 'name')


# Init schema
section_schema = SectionSchema()
sections_schema = SectionSchema(many=True)
students_schema = StudentSchema(many=True)
