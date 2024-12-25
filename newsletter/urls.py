from django.urls import path

from .views import newsletter_subscription

urlpatterns = [
    path("newsletter/create/", newsletter_subscription, name="newsletter_create"),
]
