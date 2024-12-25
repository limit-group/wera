from django import forms

from form_mtaani.models import FormMtaani


class FormMtaaniForm(forms.ModelForm):
    class Meta:
        model = FormMtaani
        fields = "__all__"
