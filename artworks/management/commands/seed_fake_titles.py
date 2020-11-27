from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _
import random

from artworks.fixtures.factories import TitleFactory
from artworks.models import Genre


class Command(BaseCommand):
    help = _('Seeds the database.')

    def add_arguments(self, parser):
        parser.add_argument(
            '--amount',
            default=205,
            type=int,
            help='The number of fake artworks to create.',
        )

    def handle(self, *args, **options):
        for _ in range(options['amount']):
            genres = []
            for _ in range(random.randint(1, 5)):
                genres.append(Genre.objects.order_by('?').first())
            TitleFactory.create(genre=tuple(genres))
