from django.shortcuts import render

from common.utils import upload_to_supabase_bucket
from contact.forms import ContactForm
from contact.models import Contact


def contact(request):
    ctx = {}
    if request.method == "GET":
        contacts = Contact.objects.all()
        ctx = {"contacts": contacts}
        return render(request, "contact/index.html", ctx)

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
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
        
        form = ContactForm()
        ctx = {"form": form}
        return render(request, "contact/index.html", ctx)


def contact_detail(request, user_id):
    contact = Contact.objects.get(user=user_id)
    ctx = {"contact": contact}
    return render(request, "contact/detail.html", ctx)
