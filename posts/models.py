from django.db import models
from django.utils.translation import gettext_lazy as _
from twitter.settings import AUTH_USER_MODEL
from django.urls import reverse_lazy
from django_jalali.db import models as jalali_models
from core.models import CreateModel, UpdateModel


class Category(CreateModel):
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    en_category_title = models.CharField(max_length=255)
    pr_category_title = models.CharField(max_length=255)
    en_category_slug = models.SlugField(max_length=150, unique=True)
    pr_category_slug = models.SlugField(max_length=150, unique=True, allow_unicode=True)
    category_image = models.ForeignKey('images.Image', related_name='category_image', on_delete=models.PROTECT,
                                       blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.pr_category_slug

    class Meta:
        db_table = _('category')
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Post(CreateModel, UpdateModel):
    category = models.ManyToManyField(Category, related_name='category_posts')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT,
                               limit_choices_to={'is_active': True, 'verify_mobile_phone': True}, )
    en_title = models.CharField(_('english title'), max_length=200)
    pr_title = models.CharField(_('persian title'), max_length=200)
    en_slug = models.SlugField(unique=True, max_length=100)
    fa_slug = models.SlugField(unique=True, max_length=100, allow_unicode=True)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    cover_image = models.ForeignKey('images.Image', on_delete=models.PROTECT, related_name='thumbnail_post',
                                    blank=True, null=True, verbose_name='cover image')
    images = models.ManyToManyField('images.Image', related_name='image_posts', verbose_name='image post')
    video = models.ManyToManyField('videos.Video', related_name='video_posts', verbose_name='video post')
    study_time = models.DurationField(blank=True, null=True)
    producer = models.ForeignKey('ProducerPost', on_delete=models.PROTECT, related_name='producer_posts')
    tag = models.ManyToManyField('Tag', related_name='tag_posts')

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'post'

    def get_absolute_url(self):
        return reverse_lazy(f'post_detail', kwargs={'pk': self.pk})


class ProducerPost(CreateModel, UpdateModel):
    producer_name = models.CharField(max_length=255)
    producer_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.producer_name

    class Meta:
        db_table = _('producer_post')
        verbose_name = _('producer_post')
        verbose_name_plural = _('producer_posts')


class Tag(CreateModel):
    tag_name = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = _('tag')
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
