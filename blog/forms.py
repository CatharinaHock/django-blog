from django import forms
from django.utils.safestring import mark_safe

from .models import Post, Tag


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "text", "authors_comment", "brief_description", "thumbnail", "tags","title_color","title_background","title_align")

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

    def clean(self):
        # data from the form is fetched using super function
        super(PostForm, self).clean()
        
        # extract the username and text field from the data
        tags = self.cleaned_data.get('tags')
        language_tags = tags.filter(type="l")

        
        # conditions to be met for the username length
        if len(language_tags) == 0:
            self._errors['tags'] = self.error_class([
                'Please choose at least one language tag.'])
        
        """
        brief_description = self.cleaned_data.get("brief_description")
        text = self.cleaned_data.get("text")
        if not brief_description:
            brief_description = text[:500]
            if len(text)<500 and not brief_description[-1] in [".", "?", "!"]:
                brief_description+=". . ."
        
        self.cleaned_data["brief_description"] = brief_description
        """

        # return any errors if found
        return self.cleaned_data

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name","style", "type")