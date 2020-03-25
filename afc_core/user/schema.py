from afc_core.manage import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar', 'role')


# Init schema
user_schema = UserSchema()
