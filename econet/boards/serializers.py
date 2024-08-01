from rest_framework import serializers
from .models import Gathering, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class GatheringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = '__all__'

class GatheringDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Gathering
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'content']

class GatheringCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = ['title', 'description', 'date', 'organizer']

class GatheringUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = ['title', 'description', 'date']
