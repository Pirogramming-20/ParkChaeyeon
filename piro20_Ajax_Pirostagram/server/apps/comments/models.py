from django.db import models
from apps.posts.models import Post
# Create your models here.
class Comment(models.Model):
  comment = models.CharField('댓글', max_length=24)
  #각 댓글이 특정 포스트에 연결되어야 함
  post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
  def __str__(self): # 파이썬의 특별한 메서드 중 하나로, 객체의 문자열 표현을 반환
    return self.comment