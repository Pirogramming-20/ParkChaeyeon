from django.db import models
from apps.tools.models import Tool
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField('제목' ,max_length=24)
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content=models.CharField('내용',max_length=24)
    interest=models.IntegerField('관심도', default=0)

   
    #tool 외래키 참조
    tool= models.ForeignKey(Tool, on_delete=models.CASCADE)
def __str__(self):
    return self.title

class PostStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)