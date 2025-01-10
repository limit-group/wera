from django.shortcuts import render

from common.utils import upload_to_supabase_bucket
from contact.forms import ProfileForm
from contact.models import Profile
from wera.models import Category


def contact(request):
    ctx = {}
    if request.method == "GET":
        contacts = Contact.objects.all()
        footer_categories = Category.get_categories()[:4]
        ctx = {"contacts": contacts, "footer_categories": footer_categories}
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


def contact_detail(request, user_id):
    profile = Profile.objects.get(user=user_id)
    ctx = {"profile": profile}
    return render(request, "profile/detail.html", ctx)
