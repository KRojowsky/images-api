from django.contrib import admin
from .models import Image, Plan, PlanFeature


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'image_thumbnail_200', 'image_thumbnail_400', 'image', 'plan')
    list_filter = ('owner', 'plan')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(PlanFeature)
class PlanFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'thumbnail_sizes', 'has_original', 'has_expiring_links')