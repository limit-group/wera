from django.urls import path

from contact import views

urlpatterns = [
    path("contacts/", views.contact, name="contacts"),
    path("contacts/<int:user_id>/", views.contact_detail, name="contact_detail"),
]
