from django.contrib import admin

from contact_me.models import ContactMe


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    pass
