from django.contrib import admin
from .models import Comment

# Register your models here.
#Post 모델을 관리자 페이지에 등록
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 보여줄 필드
    list_display = ('comment')
    #정렬,검색 기능 여기에 추가
