from django.urls import path

from wera.views import (
    cookie_policy,
    index,
    privacy_policy,
    report_a_problem,
    weras,
    wera_create,
    wera_detail,
    search_wera,
    advertising,
)

urlpatterns = [
    path("", index, name="home"),
    path("weras/", weras, name="weras"),
    path("weras-create/", wera_create, name="wera_create"),
    path("weras/<int:pk>/", wera_detail, name="wera_detail"),
    path("search/", search_wera, name="search_wera"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("privacy-policy/", cookie_policy, name="cookie_policy"),
    path("advertising/", advertising, name="advertising"),
    path("report-a-problem/", report_a_problem, name="report_a_problem"),
]
