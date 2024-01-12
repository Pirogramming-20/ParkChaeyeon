from django.urls import path
from .views import *

urlpatterns = [
    path('',movies_list), # views.py내의 함수==기능 과 연결
    path('<int:pk>',movies_read),
    path('create',movies_create), 
    path('<int:pk>/update',movies_update), 
    path('<int:pk>/delete',movies_delete),
]
