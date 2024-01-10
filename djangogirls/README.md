DJANGO 

VENV라는 가상환경
Venv (virtual environment) 라는 가상환경을 만든다 (각 플젝마다 1개씩)
	python -m venv venv(myvenv)

가상환경에 들어가기와 
	source venv(myvenv)/Scripts/activate
	실수했을때 deactivate 해줘야함

pip list로 설치된 패키지 확인 후 django설치
	pip install django
git clone 받고 각자의 venv를 만든다. 장고 설치 후 (팀장이 올려둔 freeze파일을 install하면  동일한 환경에서 개발 가능)
무거워서 .gitignore 에 ADD 필수( .gitignore에 들어갈 내용은 구글링)
서버로 들어가 로켓 뜨는지 확인 서버를 끌때는 control c를 해야함 url을 끈다고 해서 서버가 꺼지는게 아니다.

서버로 들어가기 실행하기
	python manage.py runserver

프로젝트 시작하기
	django admin startproject (mysite #프로젝트 이름#) .

앱 만들기 +settings.py에 등록
	django-admin startapp (blog #앱이름#)
	'blog',

Django 실행 흐름
url이란 ? (네트워크 상 자원 위치)
	(새로 만든 프로젝트 내 )url.py 어떤 url에 들어가면 어떤 view가 나오는지 
	view에서 model(객체화된 데이터) 사용 not mandatory (html css만 필요할수도)
	urls.py => view =>model =>template=>view

앱엔 urls.py 없다
	파일 만들어주기

프로젝트 내 urls.py에 앱의 urls.py연결
	import incude 추가
	path('', include('blog.urls')),

왜 앱과 프로젝트 각각 url을  만들고 연결해야 하는지?
	목적과 기능별로 앱을 만들기 때문에 많은 앱의 url 분업, 분리

앱의 urls.py에 view와 연결 
    from . import views

앱의 view에서 templates로 연결
	from django.shortcuts import render
	def post_list(request):
    		return render(request, 'blog/post_list.html', {})
	
앱의 modlels.py 코드 저장후 데이터베이스에 옮기기 위해
	python manage.py migrate blog