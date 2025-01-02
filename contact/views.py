from django.shortcuts import render

from contact.forms import ContactForm
from contact.models import Contact


def contact(request):
    ctx = {}
    if request.method == "GET":
        contacts = Contact.objects.all()
        ctx = {"contacts": contacts}
        return render(request, "contact/index.html", ctx)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return render(request, "contact/index.html")
        else:
            form = ContactForm()
            ctx = {"form": form}
            return render(request, "contact/index.html", ctx)


def contact_detail(request, user_id):
    contact = Contact.objects.get(user=user_id)
    ctx = {"contact": contact}
    return render(request, "contact/detail.html", ctx)
