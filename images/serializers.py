from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    thumbnails = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'image', 'thumbnails', 'account_tier']

    def get_thumbnails(self, obj):
        return obj.get_thumbnails()