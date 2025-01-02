from django.urls import path

from wera.views import index, weras, wera_create, wera_detail, search_wera

urlpatterns = [
    path("", index, name="home"),
    path("weras/", weras, name="weras"),
    path("wera/create/", wera_create, name="wera_create"),
    path("wera/<int:pk>/", wera_detail, name="wera_detail"),
    path("search/", search_wera, name="search_wera"),
]
