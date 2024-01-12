from django.db import models

# Create your models here.

class Reviews (models.Model):
    title=models.CharField(max_length=32)
    genre=models.CharField(max_length=32)
    rating=models.CharField(max_length=32)
    #year=models.CharField(max_length=32)
    #content=models.TextField()