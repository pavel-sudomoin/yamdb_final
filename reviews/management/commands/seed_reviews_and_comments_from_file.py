from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _
import csv
import os
from django.conf import settings
from django.db.utils import IntegrityError

from artworks.models import Title
from reviews.models import Review, Comment
from users.models import User


class Command(BaseCommand):
    help = _('Seeds the database from file.')

    def handle(self, *args, **options):
        filename = os.path.join(
            settings.BASE_DIR, os.path.join('data', 'review.csv')
        )
        fields = ['id', 'title_id', 'text', 'author', 'score', 'pub_date']
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                dictionary = dict(zip(fields, row))
                try:
                    dictionary['title'] = Title.objects.get(
                        id=dictionary['title_id']
                    )
                    del dictionary['title_id']

                    dictionary['author'] = User.objects.get(
                        id=dictionary.get('author')
                    )

                    Review.objects.create(**dictionary)
                except (ValueError, IntegrityError):
                    pass

        filename = os.path.join(
            settings.BASE_DIR, os.path.join('data', 'comments.csv')
        )
        fields = ['id', 'review_id', 'text', 'author', 'pub_date']
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                dictionary = dict(zip(fields, row))
                try:
                    dictionary['review'] = Review.objects.get(
                        id=dictionary['review_id']
                    )
                    del dictionary['review_id']

                    dictionary['author'] = User.objects.get(
                        id=dictionary.get('author')
                    )

                    Comment.objects.create(**dictionary)
                except ValueError:
                    pass
