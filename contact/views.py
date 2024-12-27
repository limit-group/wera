from django.shortcuts import render

from contact.models import Contact


def contact(request):
    if request.method == "GET":
        contacts = Contact.objects.all()
        ctx = {"contacts": contacts}
        return render(request, "contact/index.html", ctx)

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        location = request.POST["location"]
        work = request.POST["work"]
        image = request.POST["image"]
        rating = request.POST["rating"]
        review = request.POST["review"]
        
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            location=location,
            work=work,
            image=image,
            rating=rating,
            review=review,
        )
        contact.save()
        return render(request, "contact/index.html")
