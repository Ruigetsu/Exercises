from django.db import models

class Post(models.Model):
    id = models.IntegerField()
    title = models.CharField()
    body = models.CharField()

    class Meta:
        ordering = ['created']
