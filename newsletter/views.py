from django.shortcuts import redirect, render

from newsletter.forms import NewsletterForm


def newsletter_subscription(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NewsletterForm()
    return render(request, "wera/index.html", {"form": form})
