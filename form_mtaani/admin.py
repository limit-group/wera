from django.contrib import admin

from form_mtaani.models import FormMtaani

# Register your models here.
@admin.register(FormMtaani)
class FormMtaaniAdmin(admin.ModelAdmin):
    pass

