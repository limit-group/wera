from django.shortcuts import redirect, render

from contact_me.forms import ContactMeForm


def contact(request):
    if request.method == "POST":
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("home")
    else:
        form = ContactMeForm()
    return render(request, "contact_me/contact.html", {"form": form})

