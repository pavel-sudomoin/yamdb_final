from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _

from artworks.fixtures.factories import GenresFactory


class Command(BaseCommand):
    help = _('Seeds the database.')

    def add_arguments(self, parser):
        parser.add_argument(
            '--amount',
            default=5,
            type=int,
            help='The number of fake genres to create.',
        )

    def handle(self, *args, **options):
        for _ in range(options['amount']):
            GenresFactory.create()
