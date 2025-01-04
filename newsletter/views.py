from django.shortcuts import redirect, render

from newsletter.forms import NewsletterForm
from wera.models import Category, Location, Wera


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
