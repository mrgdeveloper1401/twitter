from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateModel, UpdateModel
from twitter.settings import AUTH_USER_MODEL
from posts.models import Post


class Comment(CreateModel, UpdateModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_comments')
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT,
                               related_name='nested_comments')

    def __str__(self):
        return f'{self.user} -- {self.post} -- {self.parent}'

    class Meta:
        db_table = 'comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Answer(CreateModel, UpdateModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='anwers')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_answers')
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT, related_name='comment_answers')
    body = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} -- {self.post} -- {self.comment}'

    class Meta:
        db_table = 'answers'
        verbose_name = _('answer')
        verbose_name_plural = _('answers')