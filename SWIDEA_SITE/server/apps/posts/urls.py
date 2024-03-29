
from django.urls import path
from .views import *

app_name='posts'
urlpatterns = [
    path('',main, name='main'),
    path('create/',create,name='create'),
    path('detail/<int:pk>/',detail, name='detail'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('update/<int:pk>/',update,name='update'),
    path('toggle_star/<int:post_id>/', toggle_post_star, name='toggle_post_star'),
]
