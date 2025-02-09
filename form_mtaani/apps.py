from django.apps import AppConfig
from watson import search


class FormMtaaniConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "form_mtaani"

    def ready(self):
        for model in self.get_models():
            search.register(model.objects.filter(active=True))
