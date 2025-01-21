from django.contrib import admin

from form_mtaani.models import FormMtaani

class FormMtaaniAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

