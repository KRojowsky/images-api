from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from images.models import Image, Plan
from images.serializers import (
    ImageSerializer,
    ThumbnailSerializer,
    ExpiringLinkSerializer,
    PlanSerializer,
)


class ImageCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ImageView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class ThumbnailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ThumbnailSerializer

    def get_object(self):
        image = generics.get_object_or_404(Image, pk=self.kwargs["pk"], user=self.request.user)
        return image.get_thumbnail(self.request.user.plan)


class ExpiringLinkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        image = generics.get_object_or_404(Image, pk=pk, user=request.user)
        serializer = ExpiringLinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        link = image.get_expiring_link(
            serializer.validated_data["expiration_time"], request.user.plan.has_exp_link_access
        )
        return Response({"link": link})


class PlanListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.filter(visible=True)