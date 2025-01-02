from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def get_locations():
        return Location.objects.all()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def get_categories():
        return Category.objects.all()


"""
Wera is a section of the home page where full time employment posts can be posted. 
Posting on the page is however restricted to users who've registered as businesses. 
The post should contain images, location and the type of job.
"""


class Wera(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE, null=True, blank=True
    )
    image = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_weras():
        return Wera.objects.order_by("-updated_at").select_related("location", "category")
