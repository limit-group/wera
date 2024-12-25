
from django.urls import path

from contact import views

urlpatterns = [
    path("contacts/", views.contact, name="contacts"),
]
