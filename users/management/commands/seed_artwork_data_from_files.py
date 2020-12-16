from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _
import csv
import os
from django.conf import settings
import codecs

from artworks.serializers import CategorySerializer, GenreSerializer
from artworks.serializers import TitleSerializer


class Command(BaseCommand):
    help = _('Seeds the database from file.')

    def handle(self, *args, **options):
        artwork_data = [
            {
                'filename': 'category.csv',
                'fields': ['id', 'name', 'slug'],
                'serializer_class': CategorySerializer,
            },
            {
                'filename': 'genre.csv',
                'fields': ['id', 'name', 'slug'],
                'serializer_class': GenreSerializer,
            },
            {
                'filename': 'titles.csv',
                'fields': ['id', 'name', 'year', 'category', 'genre'],
                'serializer_class': TitleSerializer,
            },
        ]
        for record in artwork_data:
            print(f'data from the file {record["filename"]}')
            filename = os.path.join(
                settings.BASE_DIR, os.path.join('data', record['filename'])
            )
            fields = record['fields']
            serializer_class = record['serializer_class']
            with codecs.open(
                filename, encoding='utf-8', errors='replace'
            ) as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(reader)
                for row in reader:
                    data = dict(zip(fields, row))
                    if 'genre' in data:
                        data['genre'] = data['genre'].split(', ')
                    serializer = serializer_class(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(data)
                        print(serializer.errors)
            print('end')
            print('----------------')
