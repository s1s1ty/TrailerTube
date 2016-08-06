from django import forms
from .models import Trailer, Message

class VideoForm(forms.ModelForm):
    class Meta:
        model = Trailer
        fields = [
            "title",
            "category",
            "release",
            "embed_link",

        ]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "name",
            "email",
            "message",
        ]
