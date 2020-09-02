from datetime import date
from rest_framework import serializers


def year_validator(year):
    today = date.today().year
    if year > today:
        raise serializers.ValidationError('Год не может быть больше нынешнего')
