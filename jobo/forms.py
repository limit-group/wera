from django import forms

from .models import Contact, Job, Newsletter


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "description",
            "salary_range",
            "desired_qualifications",
            "benefits",
            "location",
            "job_nature",
            "category",
            "experience",
            "gender",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "desired_qualifications": forms.Textarea(attrs={"rows": 3}),
            "benefits": forms.Textarea(attrs={"rows": 2}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email", "is_subscribed"]
