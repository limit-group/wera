from django.db import models

from wera.models import Category

"""
Form mtaani is a social tweeting page where any user can tweet out Wera findings. 
It's mainly a platform for part-time Weras around users' location. 
It contains a search bar, a Wera search filter and a location search filter.

Form mtaani tweets:
i) Has no images
ii) Should have a location and Wera type (for easy searching)
iii) Not exceed 30 words (for easy reading)

"""

class FormMtaani(models.Model):
    form = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    Wera_type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    uppdated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_weras():
        return FormMtaani.objects.all()
