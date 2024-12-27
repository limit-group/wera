from django.urls import path

from form_mtaani.views import (
    form_mtaani,
    form_mtaani_create,
    form_mtaani_detail,
)

urlpatterns = [
    path("form_mtaani/", form_mtaani, name="form_mtaani"),
    path("form_mtaani_create/", form_mtaani_create, name="form_mtaani_create"),
    path("form_mtaani_detail/<int:pk>/", form_mtaani_detail, name="form_mtaani_detail"),
]
