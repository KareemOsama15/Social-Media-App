from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """creates a new model object from models.py"""
    content = CharField(label='',
                        widget=forms.Textarea(attrs={
                            'rows': '3',
                        'placeholder': 'Say something...'
                        }))

    class Meta:
        """conatins the data we want at the form"""
        model = Post
        fields = ['content']
