import os
import uuid
from datetime import datetime, timedelta
from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse


def thumbnail_maker(image_path):
    """
    This function generates a thumbnail for the given image.
    """
    thumbnail_size = (200, 200)
    thumbnail_name = f'thumbnail_{os.path.basename(image_path)}'
    thumbnail_path = os.path.join(settings.MEDIA_ROOT, thumbnail_name)
    with Image.open(image_path) as img:
        img.thumbnail(thumbnail_size)
        img.save(thumbnail_path)
    return thumbnail_name


def generate_expiring_link(image_obj):
    """
    This function generates an expiring link for the given image object.
    """
    expiration_time = datetime.utcnow() + timedelta(minutes=10)
    uuid_str = str(uuid.uuid4())
    url = reverse('image_download', kwargs={'uuid_str': uuid_str})
    url_with_token = f"{url}?token={image_obj.generate_download_token(expiration_time)}"
    return url_with_token


class OverwriteStorage(FileSystemStorage):
    """
    This storage class overwrites any file with the same name in the destination directory.
    """
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name