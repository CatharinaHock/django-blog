from django import forms

from .models import Post, Language

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "authors_comment", "brief_description", "thumbnail")

    
    language = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox", "type": "radio"}),
        initial = ["English"],
    )