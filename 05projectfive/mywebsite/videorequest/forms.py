from .models import Video
from django import forms


class VideoForm(forms.Form):
    videoname = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Name',
                                    'id': 'inputName',
                                }))
    videodesc = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '5',
        'id': 'Comment',
        'placeholder': 'Comment'
    }))