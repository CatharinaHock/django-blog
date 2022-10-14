from django import forms

from .models import Post, Language, Tag


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "text", "authors_comment", "brief_description", "thumbnail", "language", "tags")
        widgets = {
            'language': forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox form-check-label", "type": "radio"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox form-check-label", "type": "radio"}),
        }

    """
    language = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox form-check-label", "type": "radio"}),
        initial = self.instance.language.all(),
    )
    """

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name","color")