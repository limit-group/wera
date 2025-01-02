from contact.models import Contact
from django import forms


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = "__all__"
