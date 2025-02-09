from allauth.account.decorators import verified_email_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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


def search(request):
    return render(request, "wera/index.html")


def index(request):
    weras = Wera.get_weras()
    locations = Location.get_locations()
    page = request.GET.get("page", 1)  # Get current page, default to 1
    paginator = Paginator(weras, 10)  # Show 10 results per page

    try:
        paginated_weras = paginator.page(page)
    except PageNotAnInteger:
        paginated_weras = paginator.page(1)  # Default to page 1 if invalid
    except EmptyPage:
        paginated_weras = paginator.page(
            paginator.num_pages
        )  # Show last page if out of range

    ctx = {
        "locations": locations,
        "weras": paginated_weras,
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/index.html", ctx)


def weras(request):
    weras = Wera.get_weras().all()

    page = request.GET.get("page", 1)  # Get current page, default to 1
    paginator = Paginator(weras, 10)  # Show 10 results per page

    try:
        paginated_weras = paginator.page(page)
    except PageNotAnInteger:
        paginated_weras = paginator.page(1)  # Default to page 1 if invalid
    except EmptyPage:
        paginated_weras = paginator.page(
            paginator.num_pages
        )  # Show last page if out of range

    categories = Category.get_categories()

    ctx = {
        "wera": paginated_weras,
        "profile": get_current_user_profile(request),
        "categories": categories,
    }

    return render(request, "wera/index.html", ctx)


# @login_required
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
    weras = Wera.get_weras()[:6]

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


def terms_of_service(request):
    ctx = {
        "profile": get_current_user_profile(request),
    }
    return render(request, "wera/terms_of_service.html", ctx)


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
    return render(request, "wera/error_500.html", ctx, status=500)
