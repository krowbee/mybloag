from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=40)
    date = models.DateField()
    post_text = models.TextField(max_length=256)
    image = models.ImageField(upload_to='blog_images/')