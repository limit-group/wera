
from django import forms

from contact_me.models import ContactMe


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

