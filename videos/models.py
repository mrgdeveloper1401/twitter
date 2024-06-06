from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateModel, UpdateModel
from twitter.settings import AUTH_USER_MODEL


class Video(CreateModel, UpdateModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_time = models.TimeField(blank=True, null=True, max_length=10)
    video_size = models.PositiveSmallIntegerField(blank=True, null=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='videos')
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'{self.title} -- {self.video_size} -- {self.video_time}'

    class Meta:
        db_table = 'video'
        verbose_name = 'Video'
        verbose_name_plural = _('Videos')
