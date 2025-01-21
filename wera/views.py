from allauth.account.decorators import verified_email_required
from django.shortcuts import redirect, render

from common.utils import upload_to_supabase_bucket
from contact.models import Profile
from wera.forms import ContactForm, NewsletterForm, WeraForm
from wera.models import Category, Location, Wera


def search_wera(request):
    query = request.GET.get("query")
    weras = Wera.objects.filter(title__icontains=query)

    ctx = {"weras": weras}
    return render(request, "wera/index.html", ctx)


def index(request):
    weras = Wera.get_weras()
    locations = Location.get_locations()

    profile = None
    if request.user.is_authenticated:
        profile = Profile.get_profile_by_user_id(request.user)

    ctx = {"locations": locations, "weras": weras, "profile": profile}
    return render(request, "wera/index.html", ctx)


def weras(request):
    weras = Wera.get_weras()
    ctx = {
        "wera": weras,
    }

    return render(request, "wera/index.html", ctx)


def wera_detail(request, slug):
    wera = Wera.objects.filter(slug=slug).select_related("category").first()
    ctx = {"wera": wera}

    return render(request, "wera/detail.html", ctx)


@verified_email_required
def wera_create(request):
    categories = Category.get_categories()
    locations = Location.get_locations()
    weras = Wera.get_weras()

    ctx = {
        "categories": categories,
        "locations": locations,
        "weras": weras,
    }

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
            return render(request, "wera/index.html", ctx)
    else:
        form = WeraForm()
        ctx["form"] = form
    return render(request, "wera/create.html", ctx)


def report_a_problem(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "wera/report_a_problem.html", {"form": form})


def newsletter_subscription(request):
    categories = Category.get_categories()
    locations = Location.get_locations()
    weras = Wera.get_weras()

    ctx = {"categories": categories, "locations": locations, "weras": weras}

    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NewsletterForm()
        ctx["form"] = form

    return render(request, "wera/index.html", ctx)


def privacy_policy(request):
    return render(request, "wera/privacy_policy.html")


def cookie_policy(request):
    return render(request, "wera/cookie_policy.html")


def advertising(request):
    return render(request, "wera/advertising.html")


def error_404(request, exception):
    return render(request, "wera/error_404.html", status=404)


def error_500(request):
    return render(request, "wera/error_505.html", status=500)
