from rest_framework import serializers
from .models import Gathering, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class GatheringSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Gathering
        fields = ['name', 'subject', 'activity_scope', 'likes', 'status', 'location', 'user_id']

class GatheringDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Gathering
        fields = ['name', 'subject', 'activity_scope', 'status', 'chat_link', 'description', 'comments', 'user_id']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'content']

class GatheringCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = ['name', 'subject', 'chat_link', 'activity_scope', 'status', 'location', 'description']
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
