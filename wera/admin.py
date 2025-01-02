from django.contrib import admin

from wera.models import Category, Location, Wera


@admin.register(Wera)
class WeraAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "location", "category")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
