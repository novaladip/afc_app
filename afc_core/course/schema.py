from afc_core.manage import ma


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'created_date', 'closed_date', 'teacher_id')


# Init schema
course_schema = CourseSchema()
