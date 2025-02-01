from allauth.account.decorators import verified_email_required
from django.shortcuts import render

from form_mtaani.forms import FormMtaaniForm
from form_mtaani.models import Category, FormMtaani
from wera.models import Location
from wera.views import get_current_user_profile


def form_mtaani(request):
    form_mtaanis = FormMtaani.get_form_mtaanis()

    ctx = {"form_mtaanis": form_mtaanis, "profile": get_current_user_profile(request)}
    return render(request, "form_mtaani/index.html", ctx)


def form_mtaani_detail(request, pk):
    form_mtaani = (
        FormMtaani.objects.filter(pk=pk).select_related("location", "category").first()
    )

    ctx = {
        "form_mtaani": form_mtaani,
        "profile": get_current_user_profile(request),
    }
    return render(request, "form_mtaani/detail.html", ctx)


@verified_email_required
def form_mtaani_create(request):
    categories = Category.get_categories()
    locations = Location.get_locations()
    form_mtaanis = FormMtaani.get_form_mtaanis()
    ctx = {
        "categories": categories,
        "locations": locations,
        "form_mtaanis": form_mtaanis,
        "profile": get_current_user_profile(request),
    }

    if request.method == "POST":
        form = FormMtaaniForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return render(request, "form_mtaani/index.html", ctx)
    else:
        form = FormMtaaniForm()
        ctx["form"] = form

    return render(request, "form_mtaani/create.html", ctx)
