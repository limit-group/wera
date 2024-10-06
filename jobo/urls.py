from django.urls import path

from jobo import views

urlpatterns = [
    path("", views.index, name="home"),
    path("jobs/", views.jobs, name="jobs"),
    path("job/create/", views.job_create_view, name="job_create"),
    path("jobdetail/<int:pk>/", views.jobdetail, name="jobdetail"),
    path("contact/", views.contact, name="contact"),
    path(
        "newsletter/create/", views.newsletter_subscribe_view, name="newsletter_create"
    ),
]
