from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _

from users.fixtures.factories import UserFactory

User = get_user_model()


class Command(BaseCommand):
    help = _('Seeds the database.')

    def add_arguments(self, parser):
        parser.add_argument(
            '--amount',
            default=45,
            type=int,
            help='The number of fake users to create.',
        )

    def handle(self, *args, **options):
        for _ in range(options['amount']):
            UserFactory.create()
