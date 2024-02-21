from django.db import models

class Post(models.Model):
    userId = models.IntegerField(default=0, null = True)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    
    def __str__ (self):
        return self.title

    class Meta:
        ordering = ["id"]
        db_table = 'posts_post'

#class User(models.Model):
    #name = models.CharField(max_length = 100 , db_index = True)

    #def __str__ (self):
        #return self.name