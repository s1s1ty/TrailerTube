from django import forms
from .models import Trailer

class VideoForm(forms.ModelForm):
    class Meta:
        model = Trailer
        fields = [
            "title",
            "category",
            "release",
            "embed_link",

        ]
