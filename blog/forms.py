from django import forms

from .models import Post, Tag


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "text", "authors_comment", "brief_description", "thumbnail", "tags",)

        widgets = {
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox form-check-label", "type": "radio"}),
        }


    """
    language = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.filter(type="l"),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox form-check-label", "type": "radio"}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.filter(type="o"),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox form-check-label", "type": "radio"}),
    )
    """

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name","style", "type")