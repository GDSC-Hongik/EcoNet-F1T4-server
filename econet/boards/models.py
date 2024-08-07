from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Gathering(models.Model):
    subject = models.CharField(max_length=100, default = '모임의 주제')  # 모임 주제
    name = models.CharField(max_length=100, default = '모임의 이름')  # 모임 이름
    activity_scope = models.CharField(max_length=10, choices=[('online', '온라인'), ('offline', '오프라인')], default = '활동 범위')  # 활동 범위
    likes = models.PositiveIntegerField(default=0)  # 좋아요 수
    status = models.CharField(max_length=10, choices=[('recruiting', '모집중'), ('closed', '마감됨')], default = '모집 상태')  # 모집 현황
    chat_link = models.CharField(max_length=255, default = '단톡방 링크')  # 모임 단톡방 링크
    description = models.TextField()  # 모임 설명
    location = models.CharField(max_length=100, default = '시 / 군 / 구')  # 활동 지역
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='gatherings')  # 작성자

    def __str__(self):
        return self.name

class Comment(models.Model):
    gathering = models.ForeignKey(Gathering, related_name='comments', on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.content