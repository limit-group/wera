from django.db import models

from wera.models import Category, Location

"""
Form mtaani is a social tweeting page where any user can tweet out Wera findings. 
It's mainly a platform for part-time Weras around users' location. 
It contains a search bar, a Wera search filter and a location search filter.

Form mtaani tweets:
i) Has no images
ii) Should have a location and job type (for easy searching)
iii) Not exceed 30 words (for easy reading)

"""


class FormMtaani(models.Model):
    form = models.CharField(max_length=30)
    location = location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.form

    def get_weras():
        return FormMtaani.objects.all()
