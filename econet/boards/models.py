from django.db import models

class Gathering(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    gathering = models.ForeignKey(Gathering, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.content