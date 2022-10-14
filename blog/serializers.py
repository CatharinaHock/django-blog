"""
from rest_framework import serializers

from .models import Language, Post

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name',)

class PostSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title',"text", "authors_comment", "brief_description", "created_date",
        "published_date", "thumbnail", "language",)
"""