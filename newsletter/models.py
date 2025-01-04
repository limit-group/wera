from django.db import models

from wera.models import WeraBaseModel


class Newsletter(WeraBaseModel):
    email = models.EmailField()
    is_subscribed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.email
