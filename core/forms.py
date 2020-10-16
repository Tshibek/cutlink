from django import forms
from .models import UrlShortcut


class ShortCutForm(forms.ModelForm):
    class Meta:
        model = UrlShortcut
        fields = ('link',)
