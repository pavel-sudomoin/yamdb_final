from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _
import csv
import os
from django.conf import settings
import codecs

from reviews.serializers import ReviewSerializer, CommentSerializer
from reviews.models import Title, Review

User = get_user_model()


class Command(BaseCommand):
    help = _('Seeds the database from file.')

    def handle(self, *args, **options):
        review_data = [
            {
                'filename': 'review.csv',
                'fields': [
                    'id', 'title_id', 'text', 'author_id', 'score', 'pub_date'
                ],
                'serializer_class': ReviewSerializer,
            },
            {
                'filename': 'comments.csv',
                'fields': ['id', 'review_id', 'text', 'author_id', 'pub_date'],
                'serializer_class': CommentSerializer,
            },
        ]
        for record in review_data:
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
                    author = User.objects.get(pk=data['author_id'])
                    serializer = serializer_class(data=data)
                    if serializer.is_valid():
                        if record['filename'] == 'review.csv':
                            title = Title.objects.get(pk=data['title_id'])
                            serializer.save(author=author, title=title)
                        if record['filename'] == 'comments.csv':
                            review = Review.objects.get(pk=data['review_id'])
                            serializer.save(author=author, review=review)
                    else:
                        print(data)
                        print(serializer.errors)
            print('end')
            print('----------------')

