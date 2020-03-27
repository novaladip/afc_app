from afc_core.manage import ma
from afc_core.user.schema import UserProfileSchema


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'created_at',
                  'close_date', 'teacher_id', 'teacher')

    teacher = ma.Nested(UserProfileSchema)


# Init schema
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
