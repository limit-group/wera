from django.contrib import admin

from wera.models import Category, Wera


@admin.register(Wera)
class WeraAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
