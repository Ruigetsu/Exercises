from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.CharField(max_length = 300)
    
    def __str__ (self):
        return self.title

    class Meta:
        ordering = ["id"]
        db_table = 'posts_post'