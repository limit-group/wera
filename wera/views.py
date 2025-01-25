from allauth.account.decorators import verified_email_required, login_required
from django.shortcuts import redirect, render

from common.utils import upload_to_supabase_bucket
from contact.models import Profile
from wera.forms import ContactForm, NewsletterForm, WeraForm
from wera.models import Category, Location, Wera


def get_current_user_profile(request):
    return (
        Profile.get_profile_by_user_id(request.user)
        if request.user.is_authenticated
        else None
    )


def search_wera(request):
    query = request.GET.get("query")
    weras = Wera.objects.filter(title__icontains=query)

    ctx = {"weras": weras}
    return render(request, "wera/index.html", ctx)


def index(request):
    weras = Wera.get_weras()
    locations = Location.get_locations()

    ctx = {
        "locations": locations,
        "weras": weras,
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/index.html", ctx)


def weras(request):
    weras = Wera.get_weras()

    location = request.GET.get('location')
    category = request.GET.get('category')
    job_type = request.GET.get('job_type')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    if location:
        weras = weras.filter(location__icontains=location)
    if category:
        weras = weras.filter(category_id=category)
    if job_type:
        weras = weras.filter(job_type=job_type)
    if min_salary:
        weras = weras.filter(salary__gte=min_salary)
    if max_salary:
        weras = weras.filter(salary__lte=max_salary)

    categories = Category.get_categories()
    ctx = {
        "wera": weras,
        "profile": get_current_user_profile(request),
        "categories": categories
    }

    return render(request, "wera/index.html", ctx)


@login_required
def wera_detail(request, slug):
    wera = Wera.objects.filter(slug=slug).select_related("category").first()
    ctx = {
        "wera": wera,
        "profile": get_current_user_profile(request),
    }

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
        "profile": get_current_user_profile(request),
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
    ctx = {
        "profile": get_current_user_profile(request),
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    ctx["form"] = form
    return render(request, "wera/report_a_problem.html", ctx)


def newsletter_subscription(request):
    categories = Category.get_categories()
    locations = Location.get_locations()
    weras = Wera.get_weras()

    ctx = {
        "categories": categories,
        "locations": locations,
        "weras": weras,
        "profile": get_current_user_profile(request),
    }

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
    ctx = {
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/privacy_policy.html", ctx)


def cookie_policy(request):
    ctx = {
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/cookie_policy.html", ctx)


def advertising(request):
    ctx = {
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/advertising.html", ctx)


def error_404(request, exception):
    ctx = {
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/error_404.html", ctx, status=404)


def error_500(request):
    ctx = {
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/error_505.html", ctx, status=500)
