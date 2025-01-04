from django.db import models
from django.contrib.auth import get_user_model

from wera.models import WeraBaseModel

User = get_user_model()


class ContactMe(WeraBaseModel):
    message = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
