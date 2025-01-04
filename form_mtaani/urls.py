from django.urls import path

from form_mtaani.views import (
    form_mtaani,
    form_mtaani_create,
    form_mtaani_detail,
)

urlpatterns = [
    path("form-mtaani/", form_mtaani, name="form_mtaani"),
    path("form-mtaani-create/", form_mtaani_create, name="form_mtaani_create"),
    path("form-mtaani-detail/<int:pk>/", form_mtaani_detail, name="form_mtaani_detail"),
]
