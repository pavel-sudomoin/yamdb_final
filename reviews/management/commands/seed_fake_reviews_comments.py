from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _

from reviews.fixtures.factories import ReviewFactory


class Command(BaseCommand):
    help = _('Seeds the database.')

    def add_arguments(self, parser):
        parser.add_argument(
            '--amount',
            default=50,
            type=int,
            help='The number of fake reviews to create.',
        )

    def handle(self, *args, **options):
        for _ in range(options['amount']):
            ReviewFactory.create()
