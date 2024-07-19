from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.IntegerField()
    content = models.CharField(max_length=300)
    created_dt = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    board_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Post'

class Scrap(models.Model):
    scrap_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    post = models.ForeignKey(Post, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Scrap'
