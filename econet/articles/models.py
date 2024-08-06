from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title