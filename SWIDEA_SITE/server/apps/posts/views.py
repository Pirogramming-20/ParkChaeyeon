from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post,PostStar
from django.http import JsonResponse

# Create your views here.
def main(request):
   
    posts = Post.objects.all()  
    ctx={'posts': posts }
    return render(request,'posts/post_list.html',ctx)


def create(request):

    if request.method=='GET':
        form=PostForm()
        ctx={
            'form':form
        }
        return render(request,'posts/post_create.html' ,ctx)
    #post 일때 
    form=PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

    return redirect('posts:main')

def detail(request,pk):
     post=Post.objects.get(id=pk)
     tool=post.tool #정참조
     related_posts=tool.post_set.all() #역참조
     ctx={'post':post,'related_posts': related_posts}
     return render(request,'posts/post_detail.html',ctx)

def delete(request,pk):
    if request.method=='POST':
        #PK에 해당하는 POST개체 조회
        Post.objects.get(id=pk).delete()
    return redirect('posts:main')
    

def update(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='GET':    
        form=PostForm(instance=post)
        ctx={'form': form ,'pk':pk}
        return render(request,'posts/post_update.html',ctx)
    
    form=PostForm(request.POST,request.FILES, instance=post)

    if form.is_valid():
        form.save()
    return redirect('posts:detail',pk)

def toggle_post_star(request, post_id):
    post = Post.objects.get(id=post_id)
    post_star, created = PostStar.objects.get_or_create(user=request.user, post=post)

    if not created:
        post_star.delete() 

    return JsonResponse({'starred': created})


