from django.shortcuts import redirect, render

from jobo.forms import ContactForm, JobForm, NewsletterForm
from jobo.models import Category, Job


def index(request):
    jobs = Job.get_jobs()
    categories = Category.get_categories()
    return render(request, "jobo/index.html", {"jobs": jobs, "categories": categories})


def jobs(request):
    jobs = Job.get_jobs()
    categories = Category.get_categories()
    return render(request, "jobo/jobs.html", {"jobs": jobs, "categories": categories})


def jobdetail(request, pk):
    job = Job.objects.filter(pk=pk)
    categories = Category.get_categories()
    return render(
        request, "jobo/jobdetails.html", {"job": job, "categories": categories}
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("home")
    else:
        form = ContactForm()
    return render(request, "jobo/contact.html", {"form": form})


def job_create_view(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("jobs")
    else:
        form = JobForm()
    return render(request, "jobo/job_create.html", {"form": form})


def newsletter_subscribe_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NewsletterForm()
    return render(request, "jobo/index.html", {"form": form})
