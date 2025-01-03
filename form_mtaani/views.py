from allauth.account.decorators import verified_email_required
from django.shortcuts import render

from form_mtaani.forms import FormMtaaniForm
from form_mtaani.models import Category, FormMtaani
from wera.models import Location


def form_mtaani(request):
    form_mtaanis = FormMtaani.get_form_mtaanis()
    categories = Category.get_categories()
    return render(
        request,
        "form_mtaani/index.html",
        {"form_mtaanis": form_mtaanis, "categories": categories},
    )


def form_mtaani_detail(request, pk):
    form_mtaani = FormMtaani.objects.filter(pk=pk).select_related(
        "location", "category"
    )
    categories = Category.get_categories()
    return render(
        request,
        "form_mtaani/detail.html",
        {"form_mtaani": form_mtaani, "categories": categories},
    )


@verified_email_required
def form_mtaani_create(request):
    categories = Category.get_categories()
    locations = Location.get_locations()
    form_mtaanis = FormMtaani.get_form_mtaanis()
    ctx = {
        "categories": categories,
        "locations": locations,
        "form_mtaanis": form_mtaanis,
    }
    if request.method == "POST":
        form = FormMtaaniForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return render("form_mtaani/index.html", ctx)
    else:
        form = FormMtaaniForm()
        ctx["form"] = form

    return render(request, "form_mtaani/create.html", ctx)
