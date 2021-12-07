from functools import update_wrapper
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    sulg=models.SlugField(max_length=100)
    body=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    status= models.IntegerField()