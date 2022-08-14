from django.db import models
from django.utils.translation import gettext_lazy as _


class DateTimeMixin(models.Model):
    inserted_at = models.DateTimeField(_("Creation date and time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Update date and time"), auto_now=True)
