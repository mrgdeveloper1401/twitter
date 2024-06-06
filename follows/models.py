from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UpdateModel, CreateModel
from twitter.settings import AUTH_USER_MODEL


class RelationUser(CreateModel):
    following = models.ForeignKey(AUTH_USER_MODEL, related_name='following', on_delete=models.PROTECT)
    followers = models.ForeignKey(AUTH_USER_MODEL, related_name='followers', on_delete=models.PROTECT)
    is_unfollowing = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.following} {self.followers} {self.is_unfollowing}'

    class Meta:
        db_table = 'relation_user'
        verbose_name = _('relation user')
        verbose_name_plural = _('relation users')