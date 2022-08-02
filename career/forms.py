from django import forms
from django.utils import timezone

from career.models import Candidateinfo
from softskillspace.utils.forms import CssForm


class Candidateform(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "max": "2014-01-01"})
    )


    phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "minlength": "9"}))

    class Meta:
        model = Candidateinfo
        exclude = ["visible"]
