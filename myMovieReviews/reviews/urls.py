from django.urls import path
from .views import *

urlpatterns = [
    path('',movies_list), # views.py내의 함수==기능 과 연결
    
]
