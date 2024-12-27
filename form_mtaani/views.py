from allauth.account.decorators import verified_email_required
from django.shortcuts import redirect, render

from form_mtaani.forms import FormMtaaniForm
from form_mtaani.models import Category, FormMtaani


def form_mtaani(request):
    form_mtaanis = FormMtaani.objects.all()
    categories = Category.get_categories()
    return render(
        request,
        "form_mtaani/index.html",
        {"form_mtaanis": form_mtaanis, "categories": categories},
    )


def form_mtaani_detail(request, pk):
    form_mtaani = form_mtaani.objects.get_or_404(pk=pk)
    categories = Category.get_categories()
    return render(
        request,
        "form_mtaani/detail.html",
        {"form_mtaani": form_mtaani, "categories": categories},
    )


# @verified_email_required
def form_mtaani_create(request):
    categories = Category.get_categories()
    ctx = {"categories": categories}
    if request.method == "POST":
        form = FormMtaaniForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("form_mtaanis")
    else:
        form = FormMtaaniForm()
        ctx["form"] = form
    return render(request, "form_mtaani/create.html", ctx)
