from django.urls import path

from wera.views import index, weras, wera_create_view, wera_detail

urlpatterns = [
    path("", index, name="home"),
    path("weras/", weras, name="weras"),
    path("wera/create/", wera_create_view, name="wera_create"),
    path("wera-detail/<int:pk>/", wera_detail, name="weradetail"),
]
