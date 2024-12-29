from allauth.account.decorators import verified_email_required
from django.shortcuts import redirect, render

from wera.forms import WeraForm
from wera.models import Category, Location, Wera


def index(request):
    weras = Wera.get_weras()
    categories = Category.get_categories()
    locations = Location.get_locations()
    ctx = {"categories": categories, "locations": locations, "weras": weras}
    return render(request, "wera/index.html", ctx)


def weras(request):
    weras = Wera.get_weras()
    categories = Category.get_categories()
    return render(
        request, "wera/index.html", {"weras": weras, "categories": categories}
    )


def wera_detail(request, pk):
    wera = Wera.objects.get(pk=pk)
    categories = Category.get_categories()
    return render(
        request,
        "wera/detail.html",
        {"wera": wera, "categories": categories},
    )


# @verified_email_required
def wera_create(request):
    categories = Category.get_categories()
    locations = Location.get_locations()
    ctx = {"categories": categories, "locations": locations}
    if request.method == "POST":
        form = WeraForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("weras")
    else:
        form = WeraForm()
        ctx["form"] = form
    return render(request, "wera/create.html", ctx)
