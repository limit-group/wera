from django.urls import path

from wera.views import (
    cookie_policy,
    index,
    newsletter_subscription,
    privacy_policy,
    report_a_problem,
    weras,
    wera_create,
    wera_detail,
    search_wera,
    advertising,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("", index, name="home"),
    path("weras/", weras, name="weras"),
    path("weras-create/", wera_create, name="wera_create"),
    path("weras/<slug:slug>/", wera_detail, name="wera_detail"),
    path("search/", search_wera, name="search_wera"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("cookie-policy/", cookie_policy, name="cookie_policy"),
    path("advertising/", advertising, name="advertising"),
    path("report-a-problem/", report_a_problem, name="report_a_problem"),
    path("newsletters", newsletter_subscription, name="newsletter_create"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="wera/robots.txt", content_type="text/plain"
        ),
    ),
]
