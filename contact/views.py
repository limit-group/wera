from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from common.choices import ACCOUNT_TYPE_CHOICES
from common.utils import upload_to_supabase_bucket
from contact.forms import ProfileForm
from contact.models import Profile
from wera.models import Category, Location


def contact(request):
    ctx = {}
    if request.method == "GET":
        contacts = Profile.objects.all()
        footer_categories = Category.get_categories()[:4]
        ctx = {
            "contacts": contacts,
            "footer_categories": footer_categories,
            "exclude_profile_check": True,
        }
        return render(request, "contact/index.html", ctx)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            ctc = form.save(commit=False)
            ctc.user = request.user

            if "image" in request.FILES:
                try:
                    image_url = upload_to_supabase_bucket(request.FILES["image"])
                except Exception as e:
                    ctx["error"] = f"Image upload failed: {str(e)}"
                    return render(request, "contact/create.html", ctx)

            ctc.image = image_url
            ctc.save()

            return render(request, "contact/index.html")

        form = ProfileForm()
        ctx = {"form": form}
        return render(request, "contact/index.html", ctx)


@login_required
def contact_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = Profile.get_profile_by_user_id(user=user)

    if request.method == "POST":
        data = request.POST.copy()
        first_name = data.pop("first_name", [""])[0].strip()
        last_name = data.pop("last_name", [""])[0].strip()

        if user.first_name != first_name or user.last_name != last_name:
            user.first_name = first_name
            user.last_name = last_name
            user.save()

        form = ProfileForm(data, request.FILES, instance=profile)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            image_url = profile.image
            if "image" in request.FILES:
                try:
                    image_url = upload_to_supabase_bucket(request.FILES["image"])
                except Exception as e:
                    ctx["error"] = f"Image upload failed: {str(e)}"
                    return render(request, "contact/detail.html", ctx)

            prof.image = image_url
            prof.save()
            return redirect("contact_detail", user_id=user_id)

    if request.method == "GET":
        form = ProfileForm(instance=profile)
        locations = Location.get_locations()
        ctx = {
            "profile": profile,
            "form": form,
            "locations": locations,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "account_type_choices": ACCOUNT_TYPE_CHOICES,
        }
        return render(request, "contact/detail.html", ctx)
