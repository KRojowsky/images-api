from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer, ImageLinkSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(methods=['GET'], detail=True)
    def thumbnail(self, request, pk=None):
        image = self.get_object()
        serializer = ImageLinkSerializer(image)
        return Response(serializer.data)