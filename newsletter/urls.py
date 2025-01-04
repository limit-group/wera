from django.urls import path

from .views import newsletter_subscription

urlpatterns = [
    path("newsletters", newsletter_subscription, name="newsletter_create"),
]
