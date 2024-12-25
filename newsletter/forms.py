
from django import forms

from newsletter.models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email", "is_subscribed"]
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Email address"}),
        }