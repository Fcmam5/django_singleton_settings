from django.db import models
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from .meta_models import SingletonModel

# TODO Add your parameters
class SiteSettings(SingletonModel):
    contact_email = models.EmailField(default='contact@domain.com')
    about_us = models.TextField()

    class Meta: 
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')

    def __str__(self):
        return str(_('Site Settings'))

    def set_cache(self):
        cache.set(self.__class__.__name__, self)