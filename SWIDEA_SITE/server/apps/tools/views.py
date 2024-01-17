from django.shortcuts import render,redirect
from .forms import ToolForm
from .models import Tool
from apps.posts.models import Post 
# Create your views here.

def tool_list(request):
    tools=Tool.objects.all()
    ctx={
            'tools':tools
        }
    return render(request, 'tools/tool_list.html',ctx)

def create(request):
    if request.method=='GET':
        form=ToolForm()
        ctx={
            'form':form
        }
        return render(request,'tools/tool_create.html' ,ctx)
    #post 일때 
    form=ToolForm(request.POST,)
    if form.is_valid():
        form.save()

    return redirect('tools:tool_list')

def detail(request,pk):
     tool=Tool.objects.get(id=pk)
     posts = Post.objects.filter(tool=tool)  
     ctx={'tool':tool,'posts': posts}
     return render(request,'tools/tool_detail.html',ctx)

def delete(request,pk):
    if request.method=='POST':
        #PK에 해당하는 POST개체 조회
        Tool.objects.get(id=pk).delete()
    return redirect('tools:tool_list')


def update(request,pk):

    tool=Tool.objects.get(id=pk)
    if request.method=='GET':   
        form=ToolForm(instance=tool)
        ctx={'form': form ,'pk':pk}
        return render(request,'tools/tool_update.html' ,ctx)

    form=ToolForm(request.POST,instance=tool)
    if form.is_valid():
        form.save()
    return redirect('tools:tool_list')

     