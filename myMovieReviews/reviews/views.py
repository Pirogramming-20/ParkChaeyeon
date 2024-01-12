from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def movies_list(request):
    reviews=Reviews.objects.all()
    context={
        "reviews" : reviews
    }
    print(reviews)

    return render(request, "movies_list.html",context)

def movies_read(request,pk):
    detail=Reviews.objects.get(id=pk)
    context={
        "reviews" : detail
    }
    return render(request,'movies_read.html',context)

def movies_create(request):
    if request.method=='POST':
        Reviews.objects.create(
            title=request.POST['title'],
            year=request.POST['year'],
            content=request.POST['content'],
        )
        return redirect("/reviews")
    return render(request,"movies_create.html")