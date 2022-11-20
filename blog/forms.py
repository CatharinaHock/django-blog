from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError

from .models import Post, Tag, Comment


class PostForm(forms.ModelForm):

    #def __init__(self, isTextPost, *args, **kwargs):
    #    super(PostForm, self).__init__(*args, **kwargs)
    #    self.isTextPost = isTextPost
    
    class Meta:
        model = Post
        #if isTextPost:
        fields = ("title", "text", "authors_comment", "brief_description", "thumbnail", "tags","show_title_in_header","show_title_below_header","title_color","title_background","title_align", "show_whole_thumbnail", "background_color")
        #else:
        #    fields = ("title", "text", "brief_description", "thumbnail", "tags", "post_type")

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

    def clean_tags(self):
        # data from the form is fetched using super function
        #super(PostForm, self).clean()
        
        tags = self.cleaned_data.get('tags')
        language_tags = tags.filter(type="l")
        
        if len(language_tags) == 0:
            self._errors['tags'] = self.error_class([
                'Please choose at least one language tag.'])
        #self.cleaned_data["post_type"] = "tex"
        
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
        return tags

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name","style", "type")


class PicturePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "brief_description", "thumbnail", "tags","post_type", "picture_orientation", "published_date",)
        
        widgets = {
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "column_checkbox form-check-label", "type": "radio"}),
        }
    
    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get('thumbnail')
        if not thumbnail:
            self._errors['thumbnail'] = self.error_class([
               'Please upload a picture or choose a different Post-type.'])
        return thumbnail
    
    def clean_post_type(self):
        post_type = self.cleaned_data.get("post_type")
        if self.cleaned_data.get("post_type")== "tex":
            self._errors["post_type"] = self.error_class(["Please choose 'artwork' or 'picture-based post'"])
        return post_type

        """
    def clean(self):
        # data from the form is fetched using super function
        super(PicturePostForm, self).clean()
        
        # extract the username and text field from the data
        thumbnail = self.cleaned_data.get('thumbnail')
        
        #if not thumbnail:
        #    self._errors['thumbnail'] = self.error_class([
        #        'Please upload a picture or choose a different Post-type.'])
        if self.cleaned_data.get("post_type")== "tex":
            self._errors["post_type"] = self.error_class(["Please choose 'artwork' or 'picture-based post'"])
        
        return self.cleaned_data
        """

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author':forms.Textarea(attrs={'rows':1,'placeholder':"Your name"}),
            'text': forms.Textarea(attrs={'rows':4, 'placeholder':'Put your comment here',}),
        }
    """
    def clean(self):
        cleaned_data = super(CommentForm,self).clean()
        if "chock" == cleaned_data.get("author"):
            raise ValidationError(
                "Please use a name that doesn't contain 'chock' to avoid confusion."
            )
            #self._errors["author"] = self.error_class(["Please choose a different name."])
        
        #return self.cleaned_data
    """
    def clean_author(self):
        author=self.cleaned_data.get("author")
        if "chock" in author or "Chock" in author:
            raise ValidationError(
                "Please use a name that doesn't contain 'chock' to avoid confusion."
            )
        return author
    