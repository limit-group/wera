from allauth.account.decorators import verified_email_required
from django.shortcuts import redirect, render

from common.utils import upload_to_supabase_bucket
from wera.forms import ContactForm, NewsletterForm, WeraForm
from wera.models import Category, Location, Wera


def search_wera(request):
    query = request.GET.get("query")
    weras = Wera.objects.filter(title__icontains=query)
    footer_categories = Category.get_categories()[:3]

    ctx = {"weras": weras, "footer_categories": footer_categories}
    return render(request, "wera/index.html", ctx)


def index(request):
    weras = Wera.get_weras()
    footer_categories = Category.get_categories()[:3]
    locations = Location.get_locations()
    ctx = {
        "footer_categories": footer_categories,
        "locations": locations,
        "weras": weras,
    }
    return render(request, "wera/index.html", ctx)


def weras(request):
    weras = Wera.get_weras()
    footer_categories = Category.get_categories()[:3]
    ctx = {"wera": weras, "footer_categories": footer_categories}

    return render(request, "wera/index.html", ctx)


def wera_detail(request, pk):
    wera = Wera.objects.filter(pk=pk).select_related("category").first()
    footer_categories = Category.get_categories()[:3]
    ctx = {"wera": wera, "footer_categories": footer_categories}

    return render(request, "wera/detail.html", ctx)


@verified_email_required
def wera_create(request):
    categories = Category.get_categories()
    footer_categories = Category.get_categories()[:3]
    locations = Location.get_locations()
    weras = Wera.get_weras()
    ctx = {
        "footer_categories": footer_categories,
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
