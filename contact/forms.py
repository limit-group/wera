from contact.models import Profile
from django import forms


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = "__all__"
