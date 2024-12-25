
from django.urls import path

from contact import views

urlpatterns = [
    path("contact_me/", views.contact, name="contact_me"),
]
