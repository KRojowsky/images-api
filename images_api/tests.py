from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Image, AccountTier

class ImageTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.basic_tier = AccountTier.objects.create(
            name='Basic',
            thumbnail_sizes={'basic': 200},
            can_view_original=False,
            can_generate_expiring_link=False