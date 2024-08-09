from django.db import models

class BbcArticle(models.Model):
    title = models.CharField(max_length=255)    # 기사 제목
    content = models.TextField(blank=True, null=True)   # 기사 본문
    date = models.DateField(blank=True, null=True)  # 기사 작성 일자
    url = models.URLField() # 기사 url 링크
    image_url = models.URLField(blank=True, null=True)  # 기사 이미지 url

    def __str__(self):
        return self.title
    
class HkbsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    url = models.URLField()
    image_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title