from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from wera.models import Category, Location, WeraBaseModel

User = get_user_model()


class FormMtaani(WeraBaseModel):
    """
    Form mtaani is a social tweeting page where any user can tweet out Wera findings.
    It's mainly a platform for part-time Weras around users' location.
    It contains a search bar, a Wera search filter and a location search filter.

    Form mtaani tweets:
    i) Has no images
    ii) Should have a location and job type (for easy searching)
    iii) Not exceed 30 words (for easy reading)

    """

    form = models.CharField(max_length=30)
    location = location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["updated_at"]

    def __str__(self) -> str:
        return self.form

    def get_form_mtaanis():
        return (
            FormMtaani.objects.order_by("-updated_at")
            .select_related("location", "category")
            .all()
        )

    def get_absolute_url(self):
        return reverse("form_mtaani_detail", args=[str(self.pk)])
