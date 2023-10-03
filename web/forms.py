from django import forms
from .models import EmergingDJ


class DJForm(forms.ModelForm):
    class Meta:
        model = EmergingDJ
        fields = [
            "dj_name",
            "music_genre",
            "bio",
            "soundcloud_link",
            "image",
        ]


class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar DJ", max_length=100)
