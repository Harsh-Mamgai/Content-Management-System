from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    content = models.TextField()
    info = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

