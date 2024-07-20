from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Board'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.IntegerField()
    content = models.CharField(max_length=300)
    created_dt = models.DateTimeField()
    likes = models.IntegerField()
    board_id = models.ForeignKey(Board, models.DO_NOTHING)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    updated_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Post'
    
    def __str__(self):
        return self.title

class Scrap(models.Model):
    scrap_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    post = models.ForeignKey(Post, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Scrap'

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Post', models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    content = models.CharField(max_length=300)
    likes = models.IntegerField()
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Comment'