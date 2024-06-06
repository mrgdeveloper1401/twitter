from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db.models import jDateTimeField


class CreateModel(models.Model):
    create_at = jDateTimeField(_('create at'), auto_now_add=True)

    class Meta:
        abstract = True


class UpdateModel(models.Model):
    update_at = jDateTimeField(_('update at'), auto_now=True)

    class Meta:
        abstract = True