
from django.urls import path

from contact import views

urlpatterns = [
    path("contact-me/", views.contact, name="contact_me"),
]
