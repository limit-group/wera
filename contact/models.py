from django.db import models

"""
Contacts page is what will bring businesses (employers) to our platform. 
Users can post once on this page and update their profile. 
The page is mainly used to advertise business/people to clients so the profiles should have an image, contact info, location and type of work.
The users could rate the profiles and review them.

"""
class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    image = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name