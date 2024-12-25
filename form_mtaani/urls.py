from django.urls import path

from form_mtaani.views import (
    index,
    form_mtaani,
    form_mtaani_create,
    form_mtaani_detail,
)

urlpatterns = [
    path("", index, name="home"),
    path("form_mtaani/", form_mtaani, name="form_mtaani"),
    path("form_mtaanicreate/", form_mtaani_create, name="form_mtaanicreate"),
    path("form_mtaanidetail/<int:pk>/", form_mtaani_detail, name="form_mtaanietail"),
]
