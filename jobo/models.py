from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def get_categories():
        return Category.objects.all()


class Job(models.Model):
    description = models.TextField(null=True, blank=True)
    salary_range = models.CharField(max_length=255, null=True, blank=True)
    desired_qualifications = models.TextField(null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    job_nature = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="jobs"
    )
    experience = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    vacancy = models.PositiveIntegerField(default=1, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_jobs():
        return Job.objects.all()


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()
    is_subscribed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.email
