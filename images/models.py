from django.db import models
from core.models import CreateModel
from hashlib import sha1


class Image(CreateModel):
    image = models.ImageField(upload_to='images/%Y/%m/%d/', height_field='image_height', width_field='image_width')
    image_width = models.CharField(max_length=8, blank=True, null=True)
    image_height = models.CharField(max_length=8, blank=True, null=True)
    image_alt = models.TextField(blank=True, null=True)
    image_hash = models.CharField(max_length=40, blank=True, null=True, unique=True)

    def hasher(self):
        hash_sh1 = sha1()
        for c in self.image.chunks():
            hash_sh1.update(c)
        self.image_hash = hash_sh1.hexdigest()

    def save(self, *args, **kwargs):
        self.hasher()
        return super(Image, self).save(*args, **kwargs)


