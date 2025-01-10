from django import forms


from common.choices import ACCOUNT_TYPE_CHOICES
from wera.models import Wera
from contact.models import Contact

from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    # L
    # account_type = forms.ChoiceField(
    #     label="Account Type (type BUSINESS or INDIVIDUAL)",
    #     choices=ACCOUNT_TYPE_CHOICES,
    #     widget=forms.Select(attrs={"class": "form-control"}),
    # )

    def save(self, request):
        user = super().save(request)
    

        Contact.objects.create(
            user=user,
            account_type='INDIVIDUAL',
        )
        return user


class WeraForm(forms.ModelForm):
    class Meta:
        model = Wera
        fields = "__all__"
