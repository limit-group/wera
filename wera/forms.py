from django import forms

from wera.models import Wera

from allauth.account.forms import SignupForm


ACCOUNT_TYPE_CHOICES = (
    ("BUSINESS", "Business"),
    ("INDIVIDUAL", "Individual"),
)


class CustomSignupForm(SignupForm):
    account_type = forms.ChoiceField(
        label="Account Type (type BUSINESS or INDIVIDUAL)",
        choices=ACCOUNT_TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def save(self, request):
        user = super().save(request)
        user.account_type = self.cleaned_data["account_type"]
        user.save()
        return user


class WeraForm(forms.ModelForm):
    class Meta:
        model = Wera
        fields = "__all__"
