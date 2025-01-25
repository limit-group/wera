from django.contrib import admin

from contact.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
