from django.urls import path
from .views import *

#이부분도 참조할때 이용된다. posts:post_list 이런식으로
app_name = 'posts'

urlpatterns = [
    #name= 뒷부분은 참조할때 쓰이는 이름
    #파이썬에서 모듈 경로는 . 을  이용
    path('', post_list, name='post_list'),
    path('post_new/', post_new, name='post_new'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('like_ajax/', like_ajax, name='like_ajax'),
]
