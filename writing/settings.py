from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

LANGUAGES = getattr(settings, 'WHISTLE_LANGUAGES', [('', '---------')] + list(settings.LANGUAGES))

