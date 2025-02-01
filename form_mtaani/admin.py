from django.contrib import admin

from form_mtaani.models import FormMtaani


@admin.register(FormMtaani)
class FormMtaaniAdmin(admin.ModelAdmin):
    pass
