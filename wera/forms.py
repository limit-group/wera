from allauth.account.forms import SignupForm
from django import forms

from common.choices import ACCOUNT_TYPE_CHOICES
from contact.models import Profile
from wera.models import Contact, Newsletter, Wera


class CustomSignupForm(SignupForm):
    # L
    # account_type = forms.ChoiceField(
    #     label="Account Type (type BUSINESS or INDIVIDUAL)",
    #     choices=ACCOUNT_TYPE_CHOICES,
    #     widget=forms.Select(attrs={"class": "form-control"}),
    # )

    def save(self, request):
        user = super().save(request)

        Profile.objects.create(
            user=user,
            account_type="INDIVIDUAL",
        )
        return user


class WeraForm(forms.ModelForm):
    class Meta:
        model = Wera
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email", "is_subscribed"]
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Email address"}),
        }
