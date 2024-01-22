from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from apps.comments.models import Comment
from .forms import PostForm

# Create your views here. 
def post_list(request): #request 는 http요청을 처리할때 사용되는 객체 , 객체란 클래스로 만들어진 붕어빵.
    #Post 에서 만든 title,content,like
    posts = Post.objects.all() #클래스인 Post 붕어빵 틀로 만든 객체 posts붕어빵
    ctx = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', ctx) #객체와 함께 보여질 화면과 정보를 전달한다

#시간되면 글 생성도 
def post_new(request):
    #양식 채워서 제출할때
    if request.method == 'POST':
        form = PostForm(request.POST)
        #양식 바로 채워져있는지
        if form.is_valid():
            form.save()
            return redirect('posts:post_list') #여기서 apps name 이용 참조해야하니까
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'posts/post_new.html', ctx)
    #게시글 만들기 페이지 방문할때
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'posts/post_new.html', ctx)

def detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})



def post_count(request):
    # 게시물 수 계산
    post_count = Post.objects.count()
    context = {
        'post_count': post_count,
    }
    return render(request, 'base.html', context)
#ajax 로 좋아요 수 늘리기
#생긴 의문점: 왜 이 부분만 json으로 바꿔주는거지 그냥 함수 만들어서 templates에 해당하는 html만들면 안되나
#해결: 전체 새로고침 X, 즉각적 결과 보여줌, 만약 ajax 이용안했으면 버튼 클릭할때마다 새로고침해야 바뀐 결과가 보여짐
    
import json #글자로 된 정보를 쓸 수 있는 형태로 바꿔줌
from django.http import JsonResponse #우리가 만든 정보를 웹페이지로 보내줄때 사용
from django.views.decorators.csrf import csrf_exempt #안전한지 확인?


@csrf_exempt # 위에 안전관련 잠깐 해제해주는 것 


#웹페이지와 서버간의 정보 교환은 json 이나 xml 데이터 형식으로 이루어지기에
def like_ajax(request):
    req=json.loads(request.body) # json 문자열을 python(우리가 동작 실행하는 함수를 만들었으니까)으로 변환하고
    post_id=req['id']

    post=Post.objects.get(id=post_id)
    post.like+=1
    post.save()

    return JsonResponse({'id':post_id,  'like': post.like}) #python을 json으로 바꿔 웹페이지에 전달한다.

