from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _
import csv
import os
from django.conf import settings

from artworks.models import Category


class Command(BaseCommand):
    help = _('Seeds the database from file.')

    def handle(self, *args, **options):
        filename = os.path.join(
            settings.BASE_DIR, os.path.join('data', 'category.csv')
        )
        fields = ['id', 'name', 'slug']
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                dictionary = dict(zip(fields, row))
                try:
                    Category.objects.create(**dictionary)
                except ValueError:
                    pass
