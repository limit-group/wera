from allauth.account.decorators import verified_email_required
from django.shortcuts import redirect, render

from form_mtaani.forms import FormMtaaniForm
from form_mtaani.models import Category, FormMtaani


def index(request):
    form_mtaani = form_mtaani.get_form_mtaani()
    categories = Category.get_categories()
    return render(
        request,
        "form_mtaani/index.html",
        {"form_mtaanis": form_mtaani, "categories": categories},
    )


def form_mtaani(request):
    form_mtaanis = FormMtaani.get_form_mtaanis()
    categories = Category.get_categories()
    return render(
        request,
        "form_mtaani/form_mtaanis.html",
        {"form_mtaanis": form_mtaanis, "categories": categories},
    )


def form_mtaani_detail(request, pk):
    form_mtaani = form_mtaani.objects.get_or_404(pk=pk)
    categories = Category.get_categories()
    return render(
        request,
        "form_mtaani/form_mtaani_detail.html",
        {"form_mtaani": form_mtaani, "categories": categories},
    )


@verified_email_required
def form_mtaani_create(request):
    if request.method == "POST":
        form = FormMtaaniForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("form_mtaanis")
    else:
        form = FormMtaaniForm()
    return render(request, "form_mtaani/form_mtaani_create.html", {"form": form})
