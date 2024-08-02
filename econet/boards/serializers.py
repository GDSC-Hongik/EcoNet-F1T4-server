from rest_framework import serializers
from .models import Gathering, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class GatheringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = ['subject', 'name', 'activity_scope', 'likes', 'status']

class GatheringDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Gathering
        fields = ['name', 'subject', 'activity_scope', 'status', 'chat_link', 'description', 'comments']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'content']

class GatheringCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = ['name', 'subject', 'activity_scope', 'status', 'chat_link', 'description', 'location']
        extra_kwargs = {
            'name': {'required': True},
            'subject': {'required': True},
            'activity_scope': {'required': True},
            'status': {'required': True},
            'location': {'required': True},
        }

class GatheringUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = ['name', 'subject', 'activity_scope', 'status', 'chat_link', 'description', 'location']
