from django.urls import path
from django.views.generic import TemplateView

from wera import views

urlpatterns = [
    path("", views.index, name="home"),
    path("weras/", views.weras, name="weras"),
    path("weras-create/", views.wera_create, name="wera_create"),
    path("weras/<slug:slug>/", views.wera_detail, name="wera_detail"),
    path("search/", views.search, name="search_wera"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("advertising/", views.advertising, name="advertising"),
    path("report-a-problem/", views.report_a_problem, name="report_a_problem"),
    path("terms-of-service/", views.terms_of_service, name="terms_of_service"),
    path("newsletters", views.newsletter_subscription, name="newsletter_create"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="wera/robots.txt", content_type="text/plain"
        ),
    ),
]
