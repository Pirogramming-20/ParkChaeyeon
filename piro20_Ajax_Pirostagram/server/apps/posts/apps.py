from django.apps import AppConfig

 #django에게 posts라는 앱이 있다고 알려주는 파일 

class PostsConfig(AppConfig): #django에서 AppConfig 클래스 가져옴
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.posts'
