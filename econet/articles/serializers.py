from rest_framework import serializers
from .models import BbcArticle, HkbsArticle

class BbcArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BbcArticle
        fields = ['id', 'title', 'content', 'date', 'url', 'image_url']

class HkbsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HkbsArticle
        fields = ['id', 'title', 'content', 'date', 'url', 'image_url']