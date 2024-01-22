from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
  path('list/', comment_list, name='list'),
  path('create/<int:post_pk>/', create, name='create'),
  path('delete/<int:post_pk>/<int:comment_pk>/', delete, name='delete'),
]