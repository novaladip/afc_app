import validator


class Validate:
    @staticmethod
    def register_student_dto(dto):
        rules = {
            "email": [validator.Required, validator.Range(1, 100)],
            "first_name": [validator.Required, validator.Range(1, 100)],
            "last_name": [validator.Required, validator.Range(1, 100)],
            "password": [validator.Required, validator.Range(6, 30)],
        }

        return validator.validate(rules, dto)
