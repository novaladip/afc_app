from afc_core.manage import ma
from afc_core.api.user.schema import UserProfileSchema


class EnrollmentStudentSchema(ma.Schema):
    class Meta:
        fields = ('student', )

    student = ma.Nested(UserProfileSchema)


class SectionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'count', 'date', )


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'created_at',
                  'close_date', 'teacher_id', 'teacher')

    teacher = ma.Nested(UserProfileSchema)


class CourseExtraSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'created_at',
                  'close_date', 'teacher_id', 'teacher', 'students', 'sections')
    teacher = ma.Nested(UserProfileSchema)
    students = ma.Nested(EnrollmentStudentSchema, many=True)
    sections = ma.Nested(SectionSchema, many=True)


# Init schema
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
course_student_schema = CourseExtraSchema()
courses_student_schema = CourseExtraSchema(many=True)
