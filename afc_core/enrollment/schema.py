from afc_core.manage import ma
from afc_core.course.schema import CourseSchema
from afc_core.user.schema import UserSchema


class EnrollmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'enroll_date', 'student_id',
                  'course_id', 'student', 'course')

    student = ma.Nested(UserSchema)
    course = ma.Nested(CourseSchema)


# Init schema
enrollment_schema = EnrollmentSchema()
enrollments_schema = EnrollmentSchema(many=True)
