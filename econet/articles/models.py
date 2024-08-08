from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)    # 기사 제목
    content = models.TextField(blank=True, null=True)   # 기사 본문
    date = models.DateField(blank=True, null=True)  # 기사 작성 일자
    url = models.URLField() # 기사 url 링크
    image_url = models.URLField(blank=True, null=True)  # 기사 이미지 url

    def __str__(self):
        return self.title