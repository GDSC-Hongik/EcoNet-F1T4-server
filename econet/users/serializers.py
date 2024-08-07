from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BoardsComment, BoardsGathering


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'nickname', 'password')

# 패스워드가 필요없는 다른 테이블에서 사용할 용도
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'nickname')



class BoardsGatheringSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardsGathering
        fields = ('id', 'description')

class BoardsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardsComment
        fields = ('id', 'content')

class UserProfileSerializer(serializers.ModelSerializer):
    posts = BoardsGatheringSerializer(many=True, read_only=True, source='user_posts')
    comments = BoardsCommentSerializer(many=True, read_only=True, source='user_comments')

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'nickname', 'image', 'posts', 'comments')