from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField('이름', max_length=24)
    kind = models.CharField('종류', max_length=24)
    content=models.CharField('내용',max_length=24)

def __str__(self):
     return self.name 