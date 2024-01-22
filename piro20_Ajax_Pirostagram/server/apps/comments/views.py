from django.shortcuts import render,redirect
from .forms import CommentForm
from .models import Comment
from apps.posts.models import Post
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
# Create your views here.
def comment_list(request):
    comments =Comment.objects.all()
    ctx = {'comments': comments}
    return render(request, 'comments/comment_list.html', ctx)

def create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:detail', pk=post_pk)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_create.html', {'form': form, 'post': post})
@require_POST
def delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    comment.delete()
    return redirect('posts:detail', pk=post_pk)
