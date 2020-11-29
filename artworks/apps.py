from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArtworksConfig(AppConfig):
    name = 'artworks'
    verbose_name = _('Artworks')
