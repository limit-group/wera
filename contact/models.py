from django.db import models
from django.contrib.auth import get_user_model


from common.choices import ACCOUNT_TYPE_CHOICES
from wera.models import Location, WeraBaseModel

User = get_user_model()


"""
Contacts page is what will bring businesses (employers) to our platform. 
Users can post once on this page and update their profile. 
The page is mainly used to advertise business/people to clients so the profiles should have an image, contact info, location and type of work.
The users could rate the profiles and review them.

"""


class Profile(WeraBaseModel):
    phone = models.CharField(max_length=100, null=True, blank=True)
    work = models.CharField(max_length=100, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    account_type = models.CharField(
        max_length=25, null=True, blank=True, choices=ACCOUNT_TYPE_CHOICES
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.user.get_full_name()
    
    class Meta:
        unique_together = ("user", "account_type")


    @classmethod
    def get_profile_by_user_id(cls, user):
        return cls.objects.filter(user=user).first()
