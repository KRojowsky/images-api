from django.urls import path

from images.views import (
    ImageCreateView,
    ImageView,
    ThumbnailView,
    ExpiringLinkView,
    PlanListView,
)


urlpatterns = [
    path("images/", ImageCreateView.as_view(), name="image_create"),
    path("images/<int:pk>/", ImageView.as_view(), name="image_detail"),
    path("images/<int:pk>/thumbnail/", ThumbnailView.as_view(), name="image_thumbnail"),
    path("images/<int:pk>/expiring-link/", ExpiringLinkView.as_view(), name="image_expiring_link"),
    path("plans/", PlanListView.as_view(), name="plan_list"),
]