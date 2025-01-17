from django.contrib.auth import get_user_model
from django.urls import reverse
from supabase import create_client
from django.conf import settings
import os
from django.db import models

User = get_user_model()


class WeraBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class Newsletter(WeraBaseModel):
    email = models.EmailField(max_length=254, unique=True)
    is_subscribed = models.BooleanField(default=True)


class Contact(WeraBaseModel):
    message = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Location(WeraBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def get_locations():
        return Location.objects.all()


class Category(WeraBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_categories(cls):
        return cls.objects.order_by("-updated_at")


"""
Wera is a section of the home page where full time employment posts can be posted. 
Posting on the page is however restricted to users who've registered as businesses. 
The post should contain images, location and the type of job.
"""


class Wera(WeraBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE, null=True, blank=True
    )
    image = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    _metadata = {
        "title": "name",
        "description": "abstract",
        "image": "get_meta_image",
    }

    class Meta:
        ordering = ["updated_at"]

    def __str__(self) -> str:
        return self.title

    def get_meta_image(self):
        if self.image:
            return self.image

    def get_weras():
        return Wera.objects.order_by("-updated_at").select_related(
            "location", "category"
        )

    def get_absolute_url(self):
        return reverse("wera_detail", args=[str(self.id)])
