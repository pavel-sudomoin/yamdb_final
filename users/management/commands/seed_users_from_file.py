from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _
import csv
import os
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    help = _('Seeds the database from file.')

    def handle(self, *args, **options):
        filename = os.path.join(
            settings.BASE_DIR, os.path.join('data', 'users.csv')
        )
        fields = [
            'id',
            'username',
            'email',
            'role',
            'bio',
            'first_name',
            'last_name',
        ]
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                dictionary = dict(zip(fields, row))
                try:
                    User.objects.create(**dictionary)
                except ValueError:
                    pass
