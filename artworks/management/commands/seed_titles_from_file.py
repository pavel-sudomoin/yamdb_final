from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _
import csv
import os
from django.conf import settings
from artworks.serializers import TitleSerializer
import codecs

class Command(BaseCommand):
    help = _('Seeds the database from file.')

    def handle(self, *args, **options):
        filename = os.path.join(
            settings.BASE_DIR, os.path.join('data', 'titles3.csv')
        )
        fields = [
            'id',
            'name',
            'year',
            'category'
        ]
        types_of_encoding = ["utf8", "cp1252"]
        for encoding_type in types_of_encoding:
            with codecs.open(filename, encoding = encoding_type, errors ='replace') as csvfile:
            #with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in reader:
                    data = dict(zip(fields, row))
                    serializer = TitleSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
