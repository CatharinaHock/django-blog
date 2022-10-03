from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "authors_comment", "brief_description", "thumbnail", "language")