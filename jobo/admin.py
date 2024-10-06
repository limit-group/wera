from django.contrib import admin

from jobo.models import Category, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
