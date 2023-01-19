from django.core.exceptions import ValidationError
import re

def validate_address_length(value):
    pattern = r'^[а-яА-Яа-zA-z0-9\ \.\,\-]*'
    if re.match(pattern, value).span()[1] != len(value):
        raise ValidationError('Строка не должна содержать специальные символы')