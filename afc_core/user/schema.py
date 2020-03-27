from afc_core.manage import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar', 'role')


class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar')


# Init schema
user_schema = UserSchema()
user_profile_schema = UserProfileSchema()
