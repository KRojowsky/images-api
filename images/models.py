import os
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from images.utils import thumbnail_maker, generate_expiring_link


def validate_file_extension(value):
    """
    Validate that the file is either PNG or JPG.
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Unsupported file extension. Please upload a PNG or JPG file.'))


class Plan(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.CharField(max_length=200)
    original_file = models.BooleanField(default=False)
    expiring_links = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', validators=[validate_file_extension])
    thumbnail_200 = models.ImageField(upload_to='thumbnails/', blank=True)
    thumbnail_400 = models.ImageField(upload_to='thumbnails/', blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    expiring_link = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Generate thumbnails
        if self.plan:
            thumbnail_sizes = [int(size.strip()) for size in self.plan.thumbnail_sizes.split(',')]
            thumbnail_maker(self.image, self.thumbnail_200, thumbnail_sizes[0])
            thumbnail_maker(self.image, self.thumbnail_400, thumbnail_sizes[1])

        # Generate expiring link
        if self.plan and self.plan.expiring_links:
            self.expiring_link = generate_expiring_link(self.image.name, settings.EXPIRING_LINK_EXPIRATION_TIME)
            self.save()

    def __str__(self):
        return self.image.name