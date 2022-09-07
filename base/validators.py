from django.core.exceptions import ValidationError


def file_size(value):
    filesize = value.size
    if filesize > 100000000: # 100 MB
        raise ValidationError('Max size is 100 mb')