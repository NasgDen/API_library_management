import re

from rest_framework.serializers import ValidationError


class PhoneValidator:
    """ Класс реализует валидацию поля phone модели Users """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile("^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
        tmp_value = dict(value).get(self.field)
        if not bool(reg.match(tmp_value)):
            raise ValidationError("Неверно указан номер телефона.")