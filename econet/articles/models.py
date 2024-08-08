from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title