from django.db import models

# Create your models here
# 클래스는 붕어빵 틀,인스턴스는 붕어빵, 매서드는 붕어빵 기능
class Post(models.Model): #django 에 있는 models.Model을 상속 받음
    #필요한 필드 우선 생각
    #제목,내용,좋아요 우선 설정
    #시간 되면 사진도 직접 첨부할 수 있게  photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    #일단 지금은 post_list.html 에 같은 사진 넣어둠
    title = models.CharField(max_length=100) 
    content = models.TextField()
    like = models.IntegerField() #좋아요 수
