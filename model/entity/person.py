from model.tools.validation import Validation

class Person:
    def __init__(self, id_, name, family, birth_date, username, password, is_locked, role):
        self.id_ = id_
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.username = username
        self.password = password
        self.is_locked = is_locked
        self.role = role

    def to_tuple(self):
        return (self.id_, self.name, self.family, self.birth_date, self.username, self.password, self.is_locked, self.role)

    def validate(self):
        validator = Validation()
        return validator.person_validator(self)
