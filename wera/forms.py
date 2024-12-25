from django import forms

from wera.models import Wera


class WeraForm(forms.ModelForm):
    class Meta:
        model = Wera
        fields = "__all__"
