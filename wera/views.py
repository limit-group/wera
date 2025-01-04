from allauth.account.decorators import verified_email_required
from django.shortcuts import redirect, render
from django.conf import settings
from django.utils import timezone
from common.utils import get_supabase_client, upload_to_supabase_bucket
from wera.forms import WeraForm
from wera.models import Category, Location, Wera


def search_wera(request):
    query = request.GET.get("query")
    weras = Wera.objects.filter(title__icontains=query)
    categories = Category.get_categories()
    return render(
        request, "wera/index.html", {"weras": weras, "categories": categories}
    )


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
    wera = Wera.objects.filter(pk=pk).select_related("category").first()
    categories = Category.get_categories()
    ctx = {"wera": wera, "categories": categories}

    return render(request, "wera/detail.html", ctx)


@verified_email_required
def wera_create(request):
    categories = Category.get_categories()
    locations = Location.get_locations()
    weras = Wera.get_weras()
    ctx = {"categories": categories, "locations": locations, "weras": weras}

    if request.method == "POST":
        form = WeraForm(request.POST, request.FILES)
        if form.is_valid():
            wera = form.save(commit=False)
            wera.user = request.user

            if "image" in request.FILES:
                try:
                    image_url = upload_to_supabase_bucket(request.FILES["image"])
                except Exception as e:
                    ctx["error"] = f"Image upload failed: {str(e)}"
                    return render(request, "wera/create.html", ctx)

            wera.image = image_url
            wera.save()
            return redirect("weras")
    else:
        form = WeraForm()
        ctx["form"] = form
    return render(request, "wera/create.html", ctx)


def error_404(request, exception):
    return render(request, "wera/error_404.html", status=404)


def error_500(request):
    return render(request, "wera/error_505.html", status=500)
